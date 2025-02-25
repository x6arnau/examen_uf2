# PostgreSQL Database Query Application

A Python application implementing the MVC (Model-View-Controller) pattern to perform flexible database queries.

## Author

- **Name**: Arnau Núñez López
- **Group**: DAM2

## Features

- Connection management to PostgreSQL databases
- Generic query system with flexible conditions
- Interactive menu interface
- Row-by-row result viewing
- Automatic error handling and rollback

## Requirements

- Python 3.x
- PostgreSQL database server
- `psycopg2` Python package

## Installation

1. Clone the repository
2. Install the required dependency:
   ```bash
   pip install psycopg2

## Project Structure

- `proven/`: Source code directory
- `config/db_config.py`: Database configuration
- `controllers/controller.py`: Controller class
- `models/model.py`: Model class
- `views/menu.py`: Menu class
- `views/menu_options.py`: MenuOptions class
- `__main__.py`: Main program

## Usage

1. Using the MenuOptions class:
    ```python
    super().__init__()
        self.add_item("Exit", "exit")
        self.add_item("Option 1", "option1")
        self.add_item("Option 2", "option2")
    ```

2. Using the Controller class:
    ```python
   """Set up menu handlers for each menu item."""
        self.view.items[0].handler = self._handle_exit
        self.view.items[1].handler = self._handle_view_data
        self.view.items[2].handler = self._handle_search
   ```

3. Handler function examples:

    ```python
    def _handle_view_data(self) -> None:
        try:
            results = self.model.get_table_data("table_name")
            self.view.display_results(results)
        except ModelError as e:
            self.view.display_error(str(e))
    ```
   
    ```python
      def _handle_search_by_id(self) -> None:
          try:
              id = input("Enter employee ID: ")
              results = self.model.get_table_data(
                  "employees",
                  "name, department",
                  ("id = %s", (id,))
              )
              self.view.display_results(results)
          except ModelError as e:
              self.view.display_error(str(e))
    ```
   
    ```python
      def _handle_search_by_name(self) -> None:
          try:
              name = input("Enter name to search: ")
              results = self.model.get_table_data(
                  "employees",
                  "id, name, department",
                  ("name LIKE %s", (f"%{name}%",))
              )
              self.view.display_results(results)
          except ModelError as e:
              self.view.display_error(str(e))
    ```
   
    ```python
      def _handle_search_department(self) -> None:
          try:
              dept = input("Enter department: ")
              salary = float(input("Enter minimum salary: "))
              results = self.model.get_table_data(
                  "employees",
                  "name, salary, department",
                  ("department = %s AND salary >= %s", (dept, salary))
              )
              self.view.display_results(results)
          except ModelError as e:
              self.view.display_error(str(e))
    ```