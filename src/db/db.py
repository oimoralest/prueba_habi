"""Defines the DB connection handler"""

from mysql.connector import connection
from mysql.connector.cursor import CursorBase

from .enums import DBConnectionValues, DBReturnCodes


class DB:
    def __init__(self) -> None:
        self.fetch = {"all": self._fetchall, "one": self._fetchone}

    def connect(self) -> int:
        """Creates a database connection"""
        try:
            self.conn: connection.MySQLConnection = connection.MySQLConnection(
                host=DBConnectionValues.HOST,
                port=DBConnectionValues.PORT,
                user=DBConnectionValues.USER,
                database=DBConnectionValues.SCHEMA,
                password=DBConnectionValues.PASS,
            )

            return DBReturnCodes.SUCCESS
        except connection.Error as err:
            # TODO: log error
            print(err)
            return DBReturnCodes.ERROR

    def close(self) -> None:
        """Closes database connection"""
        self.conn.close()

    def _fetchall(self):
        """Executes cursor fetchall"""
        return self.cursor.fetchall()

    def _fetchone(self):
        """Executes cursor fetchone"""
        return self.cursor.fetchone()

    def _open_cursor(self) -> None:
        """Opens a cursor to execute queries"""
        self.cursor: CursorBase = self.conn.cursor(buffered=True)

    def _close_cursor(self) -> None:
        """Closes an open cursor"""
        self.cursor.close()

    def execute_n_fetch(
        self, query: str, binds: tuple | None = None, method: str = "all"
    ):
        """Executes and fetch from a query

        :param query: Query to execute
        :param binds: Binds for filter conditions
        """
        rows = None

        try:
            self._open_cursor()

            self.cursor.execute(operation=query, params=binds)

            rows = self.fetch[method]()

            self._close_cursor()

        except connection.DatabaseError as err:
            # TODO: log error executing query
            print(err)

        return rows

    def execute_n_fetchall(self, query: str, binds: tuple | None = None):
        """Executes an fetch from a query and fetch all the rows

        :param query: Query to execute
        :param binds: Binds for filter conditions
        """
        return self.execute_n_fetch(query, binds)

    def execute_n_fetchone(self, query: str, binds: tuple | None = None):
        """Executes an fetch from a query and fetch a row

        :param query: Query to execute
        :param binds: Binds for filter conditions
        """
        return self.execute_n_fetch(query, binds, "one")
