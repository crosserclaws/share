import typing
from collections.abc import Iterable
from unittest import mock

import pytest

from allocation.adapters import repository
from allocation.domain import model
from allocation.service_layer import services, unit_of_work


class FakeRepository(repository.AbstractRepository):
    def __init__(self, products: Iterable[model.Product]) -> None:
        super().__init__()
        self._products = set(products)

    def _add(self, product: model.Product):
        self._products.add(product)

    def _get(self, sku: str) -> typing.Optional[model.Product]:
        return next((p for p in self._products if p.sku == sku), None)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self) -> None:
        self.products = FakeRepository([])
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass


def test_add_batch_for_new_product():
    uow = FakeUnitOfWork()

    services.add_batch("b1", "OMINOUS-MIRROR", 100, None, uow)

    assert uow.products.get(sku="OMINOUS-MIRROR") is not None
    assert uow.committed


def test_add_batch_for_existing_product():
    uow = FakeUnitOfWork()

    services.add_batch("b1", "EXIST-MIRROR", 100, None, uow)
    services.add_batch("b2", "EXIST-MIRROR", 100, None, uow)

    assert "b2" in [b.reference for b in uow.products.get(
        sku="EXIST-MIRROR").batches]


def test_allocate_returns_allocation():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "COMPLICATED-LAMP", 100, None, uow)

    result = services.allocate("o1", "COMPLICATED-LAMP", 10, uow)

    assert result == "b1"


def test_allocate_errors_for_invalid_sku():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "AREALSKU", 100, None, uow)

    with pytest.raises(services.InvalidSku, match="Invalid sku NONEXISTENTSKU"):
        services.allocate("o1", "NONEXISTENTSKU", 10, uow)


def test_allocate_commits():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "OMINOUS-MIRROR", 100, None, uow)
    uow.committed = False

    services.allocate("o1", "OMINOUS-MIRROR", 10, uow)

    assert uow.committed


def test_sends_email_on_out_of_stock_error():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "EMAIL-SKU", 9, None, uow)

    with mock.patch("allocation.adapters.email.send_mail") as mock_send_email:
        services.allocate("o1", "EMAIL-SKU", 10, uow)
        assert mock_send_email.call_args == mock.call(
            "stock@made.com",
            "Out of stock for EMAIL-SKU",
        )
