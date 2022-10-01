from dataclasses import dataclass
from typing import Any

from .base import DatabaseRecord


@dataclass
class CasaDatabaseRecord(DatabaseRecord):
    address: str
    city: str
    year: int
    status: str
    price: float
    description: str

    def insert(self) -> None:
        """Inserts the record in the database"""
        raise NotImplementedError

    def delete(self, id: Any) -> None:
        """deletes the record from the database"""
        raise NotImplementedError

    def update(self) -> None:
        """Updates the record in the database"""
        raise NotImplementedError

    def read(self, id: Any) -> None:
        """Read the record from the database"""
        raise NotImplementedError
