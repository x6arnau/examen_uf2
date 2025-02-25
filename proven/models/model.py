# proven/models/model.py
from proven.config.db_config import DatabaseConnection


class Model:
    """
    Data model class for storing and managing application data.
    author: Arnau Núñez López
    grup: DAM2

    Attributes:
        _data: Private attribute to store data
        db: Database connection instance
    """

    def __init__(self):
        """Initialize model with empty data and database connection."""
        self._data = None
        self.db = DatabaseConnection()

    def connect_to_db(self):
        """
        Establish database connection.

        Returns:
            bool: True if connection successful, False otherwise
        """
        return self.db.connect()

    def disconnect_from_db(self):
        """Close database connection."""
        self.db.disconnect()

    def execute_query(self, query, params=None):
        """
        Execute database query.

        Args:
            query (str): SQL query to execute
            params (tuple, optional): Query parameters

        Returns:
            Query results or None if error occurs
        """
        return self.db.execute_query(query, params)

    def generic_query(self, table_name="table", columns="*", conditions=None):
        """
        Execute a generic SELECT query on the database and display results one by one.

        Args:
            table_name (str): Name of the table to query
            columns (str): Columns to select, defaults to all
            conditions (tuple): Optional WHERE clause conditions and parameters

        Returns:
            bool: True if query executed successfully, False otherwise
        """
        try:
            query = f"SELECT {columns} FROM {table_name}"
            if conditions:
                query += f" WHERE {conditions[0]}"
                params = conditions[1]
            else:
                params = None

            results = self.execute_query(query, params)
            if results:
                print(f"\nQuery results from {table_name}:")
                print("Press Enter to see each result (or 'q' to quit):")
                for row in results:
                    user_input = input()
                    if user_input.lower() == 'q':
                        break
                    print(row)
                return True
            print("No results found")
            return False
        except Exception as e:
            print(f"Error executing query: {e}")
            return False

    def get_data(self):
        """
        Retrieve stored data.

        Returns:
            The stored data value
        """
        return self._data

    def set_data(self, data):
        """
        Set new data value.

        Args:
            data: New data value to store
        """
        self._data = data
