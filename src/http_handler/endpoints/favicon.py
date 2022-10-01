"""Defines endpoint for /favicon.ico path"""

from .base import EndpointBase


class FaviconEndpoint(EndpointBase):
    """Class to handle /favicon.ico endpoint"""

    def get(self):
        self._headers = {
            "Content-Type": "image/x-icon",
            "Content-length": 0,
        }

        self._response = 200

    def patch(self):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
