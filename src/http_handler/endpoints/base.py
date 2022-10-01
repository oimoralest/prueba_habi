"""Defines the base class used by all the endpoints"""

from abc import ABC, abstractmethod
from typing import Union

from src.db import DB


class EndpointBase(ABC):
    def __init__(self, db) -> None:
        self._response: int = 200
        self._headers: dict = {}
        self._json: str = ""

        self._db: DB = db

    @staticmethod
    def to_dict(keys, values) -> dict:
        """Creates a dictionary for the given keys and values"""
        return {key: value for key, value in zip(keys, values)}

    @abstractmethod
    def get(self, params: Union[dict, None] = None) -> None:
        """Handles get request"""
        pass

    @abstractmethod
    def post(self) -> None:
        """Handles post request"""
        pass

    @abstractmethod
    def patch(self) -> None:
        """Handles patch request"""
        pass

    @abstractmethod
    def delete(self) -> None:
        """Handles delete request"""
        pass
