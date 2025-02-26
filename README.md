# PostgreSQL Database Query Application Template

## Author

- **Name**: Arnau Núñez López
- **Group**: DAM2

## Requirements

- Python 3.x
- PostgreSQL database server Odoo 14
- `psycopg2` Python package

## Installation 🚀

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

## How to implement a new query? 🤔

1. Modify the views/menu_options.py class:
- Add a new menu item with a label and an action.
   ```python
   def __init__(self):
       """Initialize main menu with default options."""
       super().__init__()
       self.add_item("Exit", "exit")
       self.add_item("Option 1", "option1")
       self.add_item("Option 2", "option2")
   ```

2. Modify the controllers/controller.py class:
- Add a new handler function for each menu item.
    ```python
    def _setup_menu(self) -> None:
        """Set up menu handlers for each menu item."""
        self.view.items[0].handler = self._handle_exit
        self.view.items[1].handler = self._handle_view_data
        self.view.items[2].handler = self._handle_search
   ```

3. New query function examples (proven/controller.py): 😎

- Simple query example:
    ```python
    def _handle_view_data(self) -> None:
        try:
            results = self.model.get_table_data("table_name")
            self.view.display_results(results)
        except ModelError as e:
            self.view.display_error(str(e))
    ```
  
- Query with join example:
    ```python
    def _handle_join_example(self) -> None:
        try:
            results = self.model.get_table_data(
                "employees e JOIN departments d ON e.department_id = d.id",
                "e.name, e.salary, d.department_name",
                ("d.department_name = %s", ("Sales",))
            )
            self.view.display_results(results)
        except ModelError as e:
            self.view.display_error(str(e))
    ```

- Query with multiples joins example:
    ```python
    def _handle_triple_join(self) -> None:
        try:
            results = self.model.get_table_data(
                "employees e " \
                "JOIN departments d ON e.department_id = d.id " \
                "JOIN positions p ON e.position_id = p.id " \
                "JOIN locations l ON d.location_id = l.id",
                "e.name, d.department_name, p.position_title, l.city",
                ("l.country = %s AND p.salary_grade > %s", ("Spain", 3))
            )
            self.view.display_results(results)
        except ModelError as e:
            self.view.display_error(str(e))
    ```

- Query with conditions example:   
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

- Query with multiple conditions exemple 1:   
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
- Query with multiple conditions exemple 2: 
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