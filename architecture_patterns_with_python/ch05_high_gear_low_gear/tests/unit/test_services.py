from datetime import date
from typing import Iterable, Optional

import pytest

from adapters import repository
from domain import model
from service_layer import services


class FakeRepository(repository.AbstractRepository):
    def __init__(self, batches: Iterable[model.Batch]):
        self._batches = set(batches)

    def add(self, batch: model.Batch):
        self._batches.add(batch)

    def get(self, reference: str):
        return next(b for b in self._batches if b.reference == reference)

    def list(self):
        return list(self._batches)

    @staticmethod
    def for_batch(ref: str, sku: str, qty: int, eta: Optional[date]=None):
        return FakeRepository([model.Batch(ref, sku, qty, eta)])


def test_returns_allocation():
    repo = FakeRepository.for_batch("b1", "COMPLICATED-LAMP", 100, eta=None)
    result = services.allocate("o1", "COMPLICATED-LAMP", 10, repo, FakeSession())
    assert result == "b1"


def test_error_for_invalid_sku():
    repo = FakeRepository.for_batch("b1", "AREALSKU", 100, eta=None)

    with pytest.raises(services.InvalidSku, match="Invalid sku NONEXISTENTSKU"):
        services.allocate("o1", "NONEXISTENTSKU", 10, repo, FakeSession())


class FakeSession:
    committed = False

    def commit(self):
        self.committed = True


def test_commits():
    repo = FakeRepository.for_batch("b1", "OMINOUS-MIRROR", 100, eta=None)
    session = FakeSession()

    services.allocate("o1", "OMINOUS-MIRROR", 10, repo, session)
    assert session.committed is True
