from .endpoints import CasasPreventaEndpoint, FaviconEndpoint


class EndpointsMap:
    GET = {
        "/favicon.ico": FaviconEndpoint,
        "/casas/preventa": CasasPreventaEndpoint,
    }
