# proven/models/model.py
from typing import Optional, Tuple, Any, List
from proven.config.db_config import DatabaseConnection, DatabaseError


class Model:
    """
    Database model class handling database operations.
    author: Arnau Núñez López
    grup: DAM2
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

    def save_results_to_file(self, results: List[Tuple], filename: str) -> None:
        """
        Save query results to a file.

        Args:
            results (List[Tuple]): Query results to save
            filename (str): Name of the file to save results to

        Raises:
            ModelError: If file operation fails
        """
        try:
            if not filename.endswith('.txt'):
                filename += '.txt'

            with open(filename, 'w', encoding='utf-8') as file:
                for row in results:
                    file.write(f"{' | '.join(str(item) for item in row)}\n")
        except IOError as e:
            raise ModelError(f"Failed to save results: {str(e)}")

    def show_results_to_file(self, results: List[Tuple], filename: str) -> None:
        """
        Save query results to a file.

        Args:
            results (List[Tuple]): Query results to read
            filename (str): Name of the file to read results to

        Raises:
            ModelError: If file operation fails
        """
        try:
            if not filename.endswith('.txt'):
                filename += '.txt'

            with open(filename, 'r', encoding='utf-8') as file:
                for row in results:
                    print(file.readline(row))
        except IOError as e:
            raise ModelError(f"Failed to save results: {str(e)}")

    def save_results_to_csv(self, results: List[Tuple], filename: str) -> None:
        """
        Save query results to a CSV file.

        Args:
            results (List[Tuple]): Query results to save

        Raises:
            ModelError: If file operation fails
        """
        try:
            if not filename.endswith('.csv'):
                filename += '.csv'
            with open(filename, 'w', encoding='utf-8') as file:
                for row in results:
                    file.write(f"{','.join(str(item) for item in row)}\n")
        except IOError as e:
            raise ModelError(f"Failed to save results: {str(e)}")

class ModelError(Exception):
    """Custom exception for model errors."""
    pass
