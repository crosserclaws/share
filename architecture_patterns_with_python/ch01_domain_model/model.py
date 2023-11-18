from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class OrderLine:
        orderid: str
        sku: str
        qty: int


class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]) -> None:
        self.reference = ref
        self.sku = sku
        self.available_quantity = qty
        self.eta = eta


    def allocate(self, line: OrderLine):
        if self.sku != line.sku:
            raise ValueError(f'Bad argument: sku should be {self.sku}, but get {line.sku}')
        if self.available_quantity < line.qty:
            raise ValueError(f'Bad arguemnt: qty should >= {self.available_quantity}, but get {line.qty}')
        self.available_quantity -= line.qty


    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
