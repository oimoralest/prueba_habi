"""Defines the http handler for REST API"""
import http.server
from urllib.parse import urlparse

from .enums import EndpointsMap


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    DB = None

    def do_GET(self) -> None:
        """Handles GET requests"""
        try:
            parse = urlparse(self.path)
            params = {}

            if parse.query != "":
                params = dict(
                    query.split("=") for query in parse.query.split("&")
                )

            endpoint = EndpointsMap.GET[parse.path](self.DB)
            endpoint.get(params)
        except KeyError:
            # TODO: log endpoint not found and content for page not found
            # Handle other possibles status response code
            self.send_header("Content-length", 0)
            self.send_response(404)
        else:
            # Response code
            self.send_response(endpoint._response)

            # Set response headers
            for k, v in endpoint._headers.items():
                self.send_header(k, v)
            self.end_headers()

            # Write JSON content
            self.wfile.write(endpoint._json.encode(encoding="utf_8"))
