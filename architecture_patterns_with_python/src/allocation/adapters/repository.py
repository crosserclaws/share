import abc
from typing import Optional
from sqlalchemy.orm import Session

from allocation.domain import model


class AbstractRepository(abc.ABC):
    seen: set[model.Product]

    def __init__(self) -> None:
        self.seen = set()

    def add(self, product: model.Product):
        self._add(product)
        self.seen.add(product)

    def get(self, sku: str) -> model.Product:
        product = self._get(sku)
        if product:
            self.seen.add(product)
        return product

    @abc.abstractmethod
    def _add(self, product: model.Product):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, sku: str) -> model.Product:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self.session = session

    def _add(self, product: model.Product):
        self.session.add(product)

    def _get(self, sku: str) -> Optional[model.Product]:
        return self.session.query(model.Product).filter_by(sku=sku).first()
