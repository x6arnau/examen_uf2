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

- Query all example:
  ```python
  self.generic_query("table_name", "column1, column2")
  ```

- Query with single condition example:
  ```python
    self.generic_query("table_name", "column1, column2, column3", ("column1 > %s", (value1,)))
    ```

- Query with multiple conditions example:
  ```python
    self.generic_query("table_name", "column1, column2", ("column1 = %s AND column2 > %s", ("value1", "value2")))
   ```

- Query with LIKE condition example:
  ```python
    self.generic_query("table_name", "column1, column2", ("column1 LIKE %s", ("value1",)))
   ```

- Query with IN condition example:
  ```python
    self.generic_query("table_name", "column1, column2", ("column1 IN %s", ("(value1, value2, value3)",)))
   ```