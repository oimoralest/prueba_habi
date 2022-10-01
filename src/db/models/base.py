from abc import ABC, abstractmethod
from typing import Any


class DatabaseRecord(ABC):
    @abstractmethod
    def insert(self) -> None:
        """Inserts the record in the database"""
        pass

    @abstractmethod
    def delete(self, id: Any) -> None:
        """deletes the record from the database"""
        pass

    @abstractmethod
    def update(self) -> None:
        """Updates the record in the database"""
        pass

    @abstractmethod
    def read(self, id: Any) -> None:
        """Read the record from the database"""
        pass
