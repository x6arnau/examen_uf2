# proven/config/db_config.py
import psycopg2
from psycopg2 import OperationalError


class DatabaseConnection:
    """
    Database connection manager for PostgreSQL.
    author: Arnau Núñez López
    grup: DAM2

    Attributes:
        connection: PostgreSQL connection instance
        cursor: Database cursor for executing queries
        view: View instance for displaying output
    """

    def __init__(self):
        """Initialize database connection parameters."""
        self.connection = None
        self.cursor = None
        self.view = None

    def connect(self):
        """
        Establish connection to PostgreSQL database.

        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.connection = psycopg2.connect(
                user="odoo",
                password="rEURO841.Turboman",
                host="192.168.56.102",
                port="5432",
                dbname="prova_empresa"
            )
            self.cursor = self.connection.cursor()
            return True
        except OperationalError as e:
            self.view.display_error(str(e))
            return False

    def disconnect(self):
        """Close database connection and cursor."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        """
        Execute SQL query with optional parameters.

        Args:
            query (str): SQL query to execute
            params (tuple, optional): Query parameters. Defaults to None.

        Returns:
            list: Query results or None if error occurs
        """
        try:
            self.cursor.execute(query, params)
            if query.lower().startswith('select'):
                results = self.cursor.fetchall()
                return results
            else:
                self.connection.commit()
                return True
        except Exception as e:
            self.view.display_error(str(e))
            self.connection.rollback()
            return None
