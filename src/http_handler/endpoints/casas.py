"""Defines endpoints for different /casas paths"""

import json

from .base import EndpointBase


class CasasEndpoint(EndpointBase):
    """Class to handle /casas endpoint"""

    @property
    def query(self):
        return self.query

    @query.setter
    def query(self, filter):
        # TODO: Implement to modify base query based on where condition
        pass

    def get(self):
        raise NotImplementedError

    def patch(self):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError


class CasasPreventaEndpoint(CasasEndpoint):
    """Class to handle /casas/preventa endpoint"""

    def get(self):
        # TODO: Querying data

        self._headers = {"Content-Type": "application/json"}

        self._json = json.dumps({"Hello": "World"})

        self._response = 200
