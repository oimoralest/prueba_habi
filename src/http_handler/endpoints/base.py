"""Defines the base class used by all the endpoints"""

from abc import ABC, abstractmethod


class EndpointBase(ABC):
    def __init__(self, db) -> None:
        self._response: int = 200
        self._headers: dict = {}
        self._json: str = ""

        self._db = db

    @abstractmethod
    def get(self):
        """Handles get request"""
        pass

    @abstractmethod
    def post(self):
        """Handles post request"""
        pass

    @abstractmethod
    def patch(self):
        """Handles patch request"""
        pass

    @abstractmethod
    def delete(self):
        """Handles delete request"""
        pass
