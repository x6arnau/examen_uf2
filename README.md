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

## Configuration

1. The database connection settings are in proven/config/db_config.py:
- `DB_NAME`: Database name
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_HOST`: Database host
- `DB_PORT`: Database port

## Project Structure

- `proven/`: Main package 
  - `db_config/`: Configuration files for the database connection
  - `controller/`: Controller classes
  - `model/`: Model classes
  - `view/`: View classes
  - `main.py`: Main application entry point

## Implementation query examples

- Query all exemple:
```python
self.generic_query("table_name", "column1, column2")
```

- Query with single condition example:
```python
self.generic_query(
                "table_name",
                "column1, column2",
                ("column1 = %s", ("value1",))
            )
```

- Query with multiple conditions example:
```python
self.generic_query(
                "table_name",
                "column1, column2",
                ("column1 = %s AND column2 > %s", ("value1", "value2"))
            )
```

- Query with LIKE condition example:
```python
self.generic_query(
                "table_name",
                "column1, column2",
                ("column1 LIKE %s", ("value1",))
            )
```

- Query with IN condition example:
```python
self.generic_query(
                "table_name",
                "column1, column2",
                ("column1 IN %s", (('value1', 'value2'),))
            )
```
