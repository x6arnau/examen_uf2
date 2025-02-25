# proven/controllers/controller.py
class Controller:
    """
    Controls the interaction between the model and view components.
    author: Arnau Núñez López
    grup: DAM2

    Attributes:
        model: The data model instance
        view: The view instance for user interface
    """

    def __init__(self, model, view):
        """
        Initialize controller with model and view.

        Args:
            model: Model instance to handle data
            view: View instance to handle UI
        """
        self.model = model
        self.view = view

    def process_request(self, action):
        """
        Process user action requests.

        Args:
            action (str): Command string representing the user action
        """
        if action == "exit":
            self.model.exit_application()
        elif action == "option1":
            self.view.display_message("Option 1 selected")
            # TODO exemple use generic_query
            self.generic_query(
                "table_name",
                "column1, column2",
                ("column1 = %s", ("value1",))
            )
        elif action == "option2":
            self.view.display_message("Option 2 selected")
            # TODO exemple use generic_query
            self.generic_query(
                "table_name",
                "column1, column2",
                ("column1 = %s AND column2 > %s", ("value1", "value2"))
            )
        else:
            self.view.display_message("Invalid action")

    def generic_query(self, table_name, columns, conditions=None):
        """
        Execute a generic database query with flexible conditions.

        Args:
            table_name (str): Name of the table to query
            columns (str): Columns to select (comma-separated string)
            conditions (tuple, optional): Tuple containing (where_clause, params)
                where_clause: SQL WHERE clause with %s placeholders
                params: Tuple of values to replace placeholders

        Examples:
            # Query all employees
            self.generic_query("employees", "id, name")

            # Query with single condition
            self.generic_query("employees", "id, name, salary",
                             ("salary > %s", (50000,)))

            # Query with multiple conditions
            self.generic_query("employees", "id, name, department",
                             ("department = %s AND salary >= %s", ("IT", 60000)))

            # Query with LIKE condition
            self.generic_query("employees", "id, name",
                             ("name LIKE %s", ('%Smith%',)))

            # Query with IN condition
            self.generic_query("employees", "id, name",
                             ("department IN %s", (('IT', 'HR'),)))

        Returns:
            bool: True if query executed successfully, False otherwise
        """
        return self.model.generic_query(table_name, columns, conditions)
