from abc import ABC, abstractmethod
from domain import PetstoreEntity as pe

class AbstractRepository(ABC):

    @abstractmethod
    def add(self, item:pe):
        raise NotImplementedError

    @abstractmethod
    def get(self, reference) -> pe:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list:
        raise NotImplementedError

class FakeRepository(AbstractRepository):

    def __init__(self, pe):
        self._pe = set(pe)

    def add(self, pe):
        self._pe.add(pe)

    def get(self, reference):
        return next(e for e in self._pe if e._id == reference)

    def list(self):
        return list(self._pe)