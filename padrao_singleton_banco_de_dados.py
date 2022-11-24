"""Somente um objeto é criado"""

import sqlite3

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('database.db')
            self.cursor = self.connection.cursor()
        return self.cursor

# Temos 2 objetos abaixo, mas somente 1 objeto é criado
db1 = Database().connect()
db2 = Database().connect()

# o print irá mostrar a seria do db1 e db2 e são os mesmo, porque somente 1 objeto é criado
print(db1, db2)
