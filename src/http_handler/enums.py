from src.http_handler.endpoints.casas import CasasEnVentaEndpoint

from .endpoints import (
    CasasEndpoint,
    CasasPreventaEndpoint,
    CasasVendidasEndpoint,
    FaviconEndpoint,
)


class EndpointsMap:
    GET = {
        "/favicon.ico": FaviconEndpoint,
        "/casas": CasasEndpoint,
        "/casas/preventa": CasasPreventaEndpoint,
        "/casas/enventa": CasasEnVentaEndpoint,
        "/casas/vendido": CasasVendidasEndpoint,
    }
