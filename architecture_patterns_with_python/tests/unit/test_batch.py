from datetime import date

from allocation.domain.model import Batch, OrderLine


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch('batch-000', sku='SMALL-TABLE', qty=5, eta=date.today())
    order_line = OrderLine(orderid='order-000', sku='SMALL-TABLE', qty=2)

    batch.allocate(order_line)

    assert batch.available_quantity == 3


def make_batch_and_line(sku: str, batch_qty: int, line_qty: int) -> tuple[Batch, OrderLine]:
    return (
        Batch('batch-001', sku, batch_qty, eta=date.today()),
        OrderLine('order-001', sku, line_qty)
    )


def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line('ELEGANT-LAMP', 20, 2)
    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = make_batch_and_line('ELEGANT-LAMP', 2, 20)
    assert small_batch.can_allocate(large_line) is False


def test_can_allocate_if_available_equal_to_required():
    batch, line = make_batch_and_line('ELEGANT-LAMP', 2, 2)
    assert batch.can_allocate(line)


def test_cannot_allocate_if_sku_do_not_match():
    batch = Batch('batch-001', 'CHEAP-CHAIR', 100, eta=None)
    different_sku_line = OrderLine('order-001', 'EXPENSIVE-TABLE', 10)
    assert batch.can_allocate(different_sku_line) is False


def test_allocation_is_idempotent():
    batch, line = make_batch_and_line('ANGULAR-DESK', 20, 2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18


def test_deallocate():
    batch, line = make_batch_and_line('EXPENSIVE-FOOTSTOOL', 20, 2)
    batch.allocate(line)
    batch.deallocate(line)
    assert batch.available_quantity == 20


def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line('DECORATIVE-TRINKET', 20, 2)
    batch.deallocate(unallocated_line)
    assert batch.available_quantity == 20