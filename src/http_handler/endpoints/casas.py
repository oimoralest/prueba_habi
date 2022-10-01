"""Defines endpoints for different /casas paths"""

import json
from typing import Union

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
        # TODO: Querying data
        query = self.select_query(" WHERE s.name = 'pre_venta' ")

        rows: Union[list(tuple), None] = self._db.execute_n_fetchall(query)
        if rows:
            for row in rows:
                print(row)

            self._headers = {"Content-Type": "application/json"}

            self._json = json.dumps({"Hello": "World"})

            self._response = 200
        else:
            self._response = 204
