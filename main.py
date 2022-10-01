import sys
from http.server import HTTPServer

from enums import HOST, PORT
from src.db.db import DB
from src.db.enums import DBReturnCodes
from src.http_handler import HTTPRequestHandler

if __name__ == "__main__":

    # Creates db connection
    db = DB()
    if db.connect() == DBReturnCodes.ERROR:
        sys.exit(DBReturnCodes.ERROR)

    # Creates and open the server
    http_handler = HTTPRequestHandler
    httpd = HTTPServer((HOST, PORT), http_handler)
    HTTPRequestHandler.DB = db
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        db.close()
