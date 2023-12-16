from datetime import date
from typing import Optional
import pytest

from sqlalchemy import text
from sqlalchemy.orm import Session

from allocation.domain import model
from allocation.service_layer import unit_of_work


def test_uow_can_retrieve_a_batch_and_allocate_to_it(session_factory):
    session = session_factory()
    insert_batch(session, "b1", "GREAT-SKU", 100, None)
    session.commit()

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        batch = uow.batches.get(reference="b1")
        line = model.OrderLine("o1", "GREAT-SKU", 10)
        batch.allocate(line)
        uow.commit()

    batchref = get_allocated_batch_ref(session, "o1", "GREAT-SKU")
    assert batchref == "b1"


def insert_batch(session: Session, ref: str, sku: str, qty: int, eta: Optional[date]) -> None:
    session.execute(
        text(
            "INSERT INTO batches (reference, sku, _purchased_quantity, eta)"
            " VALUES "
            '(:ref, :sku, :qty, :eta)'
        ),
        dict(ref=ref, sku=sku, qty=qty, eta=eta)
    )


def get_allocated_batch_ref(session: Session, orderid: str, sku: str) -> str:
    [[ref]] = session.execute(
        text(
            "SELECT b.reference"
            " FROM batches AS b"
            " JOIN allocations AS a"
            " ON b.id = a.batch_id"
            " JOIN order_lines AS o"
            " ON o.id = a.orderline_id"
            ' WHERE orderid=:orderid AND o.sku=:sku'
        ),
        dict(orderid=orderid, sku=sku)
    )
    return ref


def test_rolls_back_uncommitted_work_by_default(session_factory):
    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)

    with uow:
        insert_batch(uow.session, "b1", "AN-SKU", 100, None)

    new_session = session_factory()
    rows = tuple(new_session.execute(text("SELECT * FROM batches")))
    assert rows == tuple()


def test_rolls_back_on_error(session_factory):
    class MyException(Exception):
        pass

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with pytest.raises(MyException):
        with uow:
            insert_batch(uow.session, "b1", "AN-SKU", 100, None)
            raise MyException

    new_session = session_factory()
    rows = tuple(new_session.execute(text("SELECT * FROM batches")))
    assert rows == tuple()
