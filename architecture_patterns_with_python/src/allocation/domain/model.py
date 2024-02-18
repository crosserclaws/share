from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional

from . import events


@dataclass(unsafe_hash=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int


class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]) -> None:
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations: set[OrderLine] = set()

    def __eq__(self, other) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self.reference == self.reference

    def __gt__(self, other) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def __hash__(self) -> int:
        return hash(self.reference)

    def __repr__(self) -> str:
        return f'<Batch {self.reference}>'

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    def deallocate_one(self) -> OrderLine:
        return self._allocations.pop()

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty


class Product:
    def __init__(self, sku: str, batches: list[Batch], version_number: int = 0):
        self.sku = sku
        self.batches = batches
        self.version_number = version_number
        self.events: list[events.Event] = []

    def allocate(self, line: OrderLine) -> Optional[str]:
        try:
            batch = next(b for b in sorted(self.batches)
                         if b.can_allocate(line))
            batch.allocate(line)
            self.version_number += 1
            return batch.reference
        except StopIteration:
            self.events.append(events.OutOfStock(line.sku))
            return None

    def change_batch_quantity(self, ref: str, qty: int) -> None:
        batch = next(b for b in self.batches if b.reference == ref)
        if batch:
            batch._purchased_quantity = qty
            while batch.available_quantity < 0:
                line = batch.deallocate_one()
                self.events.append(events.AllocationRequired(line.orderid, line.sku, line.qty))