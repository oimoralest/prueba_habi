from .endpoints import CasasEndpoint, CasasPreventaEndpoint, FaviconEndpoint


class EndpointsMap:
    GET = {
        "/favicon.ico": FaviconEndpoint,
        "/casas": CasasEndpoint,
        "/casas/preventa": CasasPreventaEndpoint,
    }
