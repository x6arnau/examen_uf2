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
- `db_config.py`: Database configuration
- `controller.py`: Controller class
- `model.py`: Model class
- `view.py`: View class
- `main.py`: Main program

## Usage

1. Using the MenuView class:
    ```python
    view = MenuView()
    view.add_item("Option Text", "command", handler_function)
    ```

2. Using the Controller class:
    ```python
   def _setup_menu(self) -> None:
       self.view.add_item("Exit", "exit", self._handle_exit)
       self.view.add_item("View Data", "view", self._handle_view_data)
       self.view.add_item("Search", "search", self._handle_search)
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