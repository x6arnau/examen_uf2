import psycopg2
from psycopg2 import OperationalError
from dataclasses import dataclass

@dataclass
class DbConfig:
    user: str = "odoo"
    password: str = "rEURO841.Turboman"
    host: str = "192.168.56.102"
    port: str = "5432"
    dbname: str = "prova_empresa"

class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self._config = DbConfig()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user=self._config.user,
                password=self._config.password,
                host=self._config.host,
                port=self._config.port,
                dbname=self._config.dbname
            )
            self.cursor = self.connection.cursor()
            return True
        except OperationalError as e:
            raise DatabaseError(f"Connection failed: {str(e)}")

    def disconnect(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except Exception as e:
            raise DatabaseError(f"Disconnect failed: {str(e)}")

    def execute_query(self, query: str, params=None):
        try:
            self.cursor.execute(query, params)
            if query.lower().strip().startswith('select'):
                return self.cursor.fetchall()
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            raise DatabaseError(f"Query execution failed: {str(e)}")

class DatabaseError(Exception):
    pass