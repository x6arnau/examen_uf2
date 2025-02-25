import psycopg2
from psycopg2 import OperationalError
from dataclasses import dataclass
from typing import Any


@dataclass
class DbConfig:
    """
    Dataclass to store database configuration details.
    author: Arnau Núñez López
    grup: DAM2

    Attributes:
        user (str): Database username.
        password (str): Database password.
        host (str): Database host address.
        port (str): Database port number.
        dbname (str): Database name.
    """
    user: str = "odoo"
    password: str = "rEURO841.Turboman"
    host: str = "192.168.56.102"
    port: str = "5432"
    dbname: str = "prova_empresa"


class DatabaseConnection:
    """
    Class to manage the database connection and operations.
    """

    def __init__(self):
        """
        Initialize database connection configuration.
        """
        self.connection = None
        self.cursor = None
        self._config = DbConfig()

    def connect(self) -> bool:
        """
        Connect to the PostgreSQL database.

        Returns:
            bool: True if connection is successful.

        Raises:
            DatabaseError: If connection fails.
        """
        try:
            self.connection = psycopg2.connect(
                user=self._config.user,
                password=self._config.password,
                host=self._config.host,
                port=self._config.port,
                dbname=self._config.dbname
            )
            self.cursor = self.connection.cursor()
            return True
        except OperationalError as e:
            raise DatabaseError(f"Connection failed: {str(e)}")

    def disconnect(self) -> None:
        """
        Disconnect from the PostgreSQL database.

        Raises:
            DatabaseError: If disconnection fails.
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except Exception as e:
            raise DatabaseError(f"Disconnect failed: {str(e)}")

    def execute_query(self, query: str, params=None) -> Any:
        """
        Execute a SQL query with optional parameters.

        Args:
            query (str): SQL query to execute.
            params (Optional[Tuple]): Query parameters.

        Returns:
            Any: Query results or success status.

        Raises:
            DatabaseError: If query execution fails.
        """
        try:
            self.cursor.execute(query, params)
            if query.lower().strip().startswith('select'):
                return self.cursor.fetchall()
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            raise DatabaseError(f"Query execution failed: {str(e)}")


class DatabaseError(Exception):
    """
    Custom exception for database errors.
    """
    pass
