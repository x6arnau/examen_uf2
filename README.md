# **Plantilla de Aplicación de Consultas a Base de Datos PostgreSQL**

## Autor 📝

- **Nombre**: Arnau Núñez López
- **Grupo**: DAM2

## Requisitos 📋

- Python 3.x
- PostgreSQL database server Odoo 14
- `psycopg2` Python package

## Instalación 🚀

1. Clona el repositorio
2. Instala la dependencia requerida:
   ```bash
   pip install psycopg2

## Estructura del Proyecto 📂

- `proven/`: Directorio de código fuente
- `config/db_config.py`: Configuración de la base de datos
- `controllers/controller.py`: Clase Controlador
- `models/model.py`: Clase Modelo
- `views/menu.py`: Clase Menu
- `views/menu_options.py`: Clase Opciones del Menú
- `__main__.py`: Programa principal

## ¿Cómo implementar una nueva consulta? 🤔

1. **Modifica** la clase `views/menu_options.py`:
- Añade un nuevo elemento al menú con una etiqueta y una acción.

```python
   def __init__(self):
  """Initialize main menu with default options."""
  super().__init__()
  self.add_item("Exit", "exit")
  self.add_item("Option 1", "option1")
  self.add_item("Option 2", "option2")
```

2. **Modifica** la clase `controllers/controller.py` class:
- Añade una nueva función manejadora para cada elemento del menú.

```python
    def _setup_menu(self) -> None:
  """Set up menu handlers for each menu item."""
  self.view.items[0].handler = self._handle_exit
  self.view.items[1].handler = self._handle_view_data
  self.view.items[2].handler = self._handle_search
```

3. **Ejemplos** de nuevas funciones de consulta (`proven/controller.py`): 😎

_- Ejemplo ejecutar una consulta (forma 1):_

```python
    def _handle_absence_days(self) -> None:
    self.view.display_message("Fetching employees with absence days greater than 5 days...")
    try:
        results = self.model.execute_query("""
            SELECT hd.name, he.name, hl.number_of_days 
            FROM hr_department hd 
            JOIN hr_employee he ON hd.id = he.department_id 
            JOIN hr_leave hl ON he.id = hl.employee_id 
            WHERE hl.number_of_days > 5
        """
        )
        self.view.display_results(results)
    except ModelError as e:
        self.view.display_error(str(e))
```

_- Ejemplo de consulta simple (forma 2):_

```python
      def _handle_view_data(self) -> None:
  try:
    results = self.model.get_table_data("table_name")
    self.view.display_results(results)
  except ModelError as e:
    self.view.display_error(str(e))
```
  
_- Ejemplo de consulta con unión (JOIN):_

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

_- Ejemplo de consulta con múltiples uniones (JOIN):_

```python
    def _handle_triple_join(self) -> None:
  try:
    results = self.model.get_table_data(
      "employees e "
      "JOIN departments d ON e.department_id = d.id "
      "JOIN positions p ON e.position_id = p.id "
      "JOIN locations l ON d.location_id = l.id",
      "e.name, d.department_name, p.position_title, l.city",
      ("l.country = %s AND p.salary_grade > %s", ("Spain", 3))
    )
    self.view.display_results(results)
  except ModelError as e:
    self.view.display_error(str(e))
```

_- Ejemplo de consulta con condiciones:_   

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

_- Ejemplo de consulta con múltiples condiciones 1:_   

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

_- Ejemplo de consulta con múltiples condiciones 2:_ 

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