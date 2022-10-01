"""Defines endpoint for /favicon.ico path"""

from typing import Union

from .base import EndpointBase


class FaviconEndpoint(EndpointBase):
    """Class to handle /favicon.ico endpoint"""

    def get(self, params: Union[dict, None] = None) -> None:
        self._headers = {
            "Content-Type": "image/x-icon",
            "Content-length": 0,
        }

        self._response = 200

    def patch(self) -> None:
        raise NotImplementedError

    def post(self) -> None:
        raise NotImplementedError

    def delete(self) -> None:
        raise NotImplementedError
