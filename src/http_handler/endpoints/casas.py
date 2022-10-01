"""Defines endpoints for different /casas paths"""

import json
from typing import Union

from src.db.models import CasaDatabaseRecord

from .base import EndpointBase
from .queries.casas import GetCasas


class CasasEndpoint(EndpointBase):
    """Class to handle /casas endpoint"""

    @staticmethod
    def select_query(
        base_filter: str = "", params: Union[dict, None] = None
    ) -> None:
        """Build the select query

        :param filter: Query filter condition
        """
        if params:
            base_filter += "AND " + " AND ".join(
                f"{key} = '{value}'" for key, value in params.items()
            )
        return GetCasas.QUERY + base_filter + " ORDER BY p.id "

    def get_casas(self, query: str) -> None:
        """Returns all the casas for a given query"""
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

    @staticmethod
    def append_casa(casa: CasaDatabaseRecord) -> bool:
        """Determines if returns a casa as a response"""
        if casa.address not in ("", None) and casa.city not in ("", None):
            return True
        return False

    def get(self, params: Union[dict, None] = None) -> None:
        self.get_casas(self.select_query(params=params))

    def patch(self) -> None:
        raise NotImplementedError

    def post(self) -> None:
        raise NotImplementedError

    def delete(self) -> None:
        raise NotImplementedError


class CasasPreventaEndpoint(CasasEndpoint):
    """Class to handle /casas/preventa endpoint"""

    def get(self, params: Union[dict, None] = None) -> None:
        base_filter: str = " WHERE s.name = 'pre_venta' "

        query: str = self.select_query(base_filter, params)

        self.get_casas(query)


class CasasEnVentaEndpoint(CasasEndpoint):
    """Class to handle /casas/enventa endpoint"""

    def get(self, params: Union[dict, None] = None) -> None:
        base_filter: str = " WHERE s.name = 'en_venta' "

        query: str = self.select_query(base_filter, params)

        self.get_casas(query)


class CasasVendidasEndpoint(CasasEndpoint):
    """Class to handle /casas/vendido endpoint"""

    def get(self, params: Union[dict, None] = None) -> None:
        base_filter: str = " WHERE s.name = 'vendido' "

        query: str = self.select_query(base_filter, params)

        self.get_casas(query)
