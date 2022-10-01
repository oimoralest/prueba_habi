"""Defines endpoints for different /casas paths"""

import json
from typing import Union

from src.db.models import CasaDatabaseRecord

from .base import EndpointBase
from .queries.casas import GetCasas


class CasasEndpoint(EndpointBase):
    """Class to handle /casas endpoint"""

    @staticmethod
    def select_query(filter: str) -> None:
        """Setter for query attribute

        :param filter: Query filter condition
        """
        return GetCasas.QUERY + filter + " ORDER BY p.id "

    def append_casa(self, casa: CasaDatabaseRecord) -> bool:
        """Determines if returns a casa as a response"""
        if casa.address not in ("", None) and casa.city not in ("", None):
            return True
        return False

    def get(self) -> None:
        raise NotImplementedError

    def patch(self) -> None:
        raise NotImplementedError

    def post(self) -> None:
        raise NotImplementedError

    def delete(self) -> None:
        raise NotImplementedError


class CasasPreventaEndpoint(CasasEndpoint):
    """Class to handle /casas/preventa endpoint"""

    def get(self) -> None:
        query: str = self.select_query(" WHERE s.name = 'pre_venta' ")

        rows: Union[list(tuple), None] = self._db.execute_n_fetchall(query)
        if rows:
            casas: list = []
            for row in rows:
                casa: dict = self.to_dict(
                    CasaDatabaseRecord.__annotations__.keys(), row
                )
                if self.append_casa(CasaDatabaseRecord(**casa)):
                    casas.append(casa)

            self._headers = {"Content-Type": "application/json"}

            self._json = json.dumps(casas)

            self._response = 200
        else:
            self._response = 204
