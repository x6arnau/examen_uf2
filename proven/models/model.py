# proven/models/model.py
from typing import Optional, Tuple, Any, List

from proven.config.db_config import DatabaseConnection, DatabaseError


class Model:
    """
    Database model class handling database operations.
    """

    def __init__(self):
        """Initialize database connection."""
        self._db = DatabaseConnection()

    def connect(self) -> bool:
        """
        Connect to the database.

        Returns:
            bool: True if connection successful
        """
        try:
            return self._db.connect()
        except DatabaseError as e:
            raise ModelError(str(e))

    def disconnect(self) -> None:
        """Disconnect from the database."""
        try:
            self._db.disconnect()
        except DatabaseError as e:
            raise ModelError(str(e))

    def execute_query(self, query: str, params: Optional[Tuple] = None) -> Any:
        """
        Execute a database query with optional parameters.

        Args:
            query (str): SQL query to execute
            params (Optional[Tuple]): Query parameters

        Returns:
            Any: Query results
        """
        try:
            return self._db.execute_query(query, params)
        except DatabaseError as e:
            raise ModelError(str(e))

    def get_table_data(self, table: str, columns: str = "*",
                     conditions: Optional[Tuple] = None) -> List[Tuple]:
        """
        Get data from a table with optional columns and conditions.

        Args:
            table (str): Table name
            columns (str): Columns to select
            conditions (Optional[Tuple]): WHERE clause and parameters

        Returns:
            List[Tuple]: Query results
        """
        query = f"SELECT {columns} FROM {table}"
        if conditions:
            query += f" WHERE {conditions[0]}"
            params = conditions[1]
        else:
            params = None
        return self.execute_query(query, params)


class ModelError(Exception):
    """Custom exception for model errors."""
    pass