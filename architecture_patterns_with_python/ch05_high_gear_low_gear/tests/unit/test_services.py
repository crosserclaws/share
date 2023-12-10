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


def test_returns_allocation():
    repo, session = FakeRepository([]), FakeSession()
    services.add_batch("b1", "COMPLICATED-LAMP", 100, None, repo, session)

    result = services.allocate("o1", "COMPLICATED-LAMP", 10, repo, FakeSession())

    assert result == "b1"


def test_error_for_invalid_sku():
    repo, session = FakeRepository([]), FakeSession()
    services.add_batch("b1", "AREALSKU", 100, None, repo, session)

    with pytest.raises(services.InvalidSku, match="Invalid sku NONEXISTENTSKU"):
        services.allocate("o1", "NONEXISTENTSKU", 10, repo, FakeSession())


class FakeSession:
    committed = False

    def commit(self):
        self.committed = True


def test_commits():
    repo, session = FakeRepository([]), FakeSession()
    services.add_batch("b1", "OMINOUS-MIRROR", 100, None, repo, session)

    services.allocate("o1", "OMINOUS-MIRROR", 10, repo, session)

    assert session.committed is True


def test_add_batch():
    repo, session = FakeRepository([]), FakeSession()

    services.add_batch("b1", "OMINOUS-MIRROR", 100, None, repo, session)

    assert repo.get("b1") is not None
    assert session.committed
