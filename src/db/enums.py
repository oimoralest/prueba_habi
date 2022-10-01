import os

from dotenv import load_dotenv

load_dotenv()


class DBConnectionValues:
    HOST = os.getenv("DBHOST")
    PORT = os.getenv("DBPORT")
    USER = os.getenv("DBUSER")
    PASS = os.getenv("DBPASS")
    SCHEMA = os.getenv("DBSCHEMA")


class DBReturnCodes:
    SUCCESS = 0
    ERROR = -1
