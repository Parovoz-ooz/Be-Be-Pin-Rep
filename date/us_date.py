import sqlite3
import os
from random import randint


class Table:
    def __init__(self):
        self.conn = sqlite3.connect('user_date.db')
        self.cursor = self.conn.cursor()

    def db_exist(self):
        if os.path.getsize('user_date.db') < 0:
            self.cursor.execute("""CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT, brain FLOAT)""")
            self.conn.commit()

            self.cursor.execute("""CREATE TABLE Module (id INTEGER PRIMARY KEY, name TEXT, progress FLOAT""")
            self.conn.commit()

            self.cursor.execute("""CREATE TABLE Lessons id INTEGER PRIMARY KEY, name TEXT, FOREIGN KEY(module_id) REFERENCES Module(id)""")
            self.conn.commit()

    def db_add(self, table_name: str, name: str, module_id: int = None, brain: float = None, progress: float = None):
        if brain:
            self.cursor.execute(f"""INSERT INTO {table_name} (id, name, brain) VALUES (1, {name}, {brain})""")
            self.conn.commit()
        elif progress:
            self.cursor.execute(f"""INSERT INTO {table_name} (1, {name}, {progress})""")
            self.conn.commit()
        elif module_id:
            self.cursor.execute(f"""INSERT INTO {table_name} (1, {name}, {"lesson1", 1})""")
            self.conn.commit()

    def db_read(self):
        self.cursor.execute("""SELECT * FROM Users""")
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)