import os
import sqlite3
from random import randint


class DB:
    def __init__(self):
        self.conn_us = sqlite3.connect('user_data.db')
        self.conn_mod = sqlite3.connect('module_data.db')
        self.conn_less = sqlite3.connect('lessons_data.db')

    def db_create(self):
        self.conn_us.execute(
            """CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, brain INTEGER NOT NULL)"""
        )
        self.conn_mod.execute(
            """CREATE TABLE module (id INTEGER PRIMARY KEY, name TEXT NOT NULL, lessons_count INTEGER NOT NULL, progress INTEGER NOT NULL)"""
        )
        self.conn_less_math.execute(
            """CREATE TABLE lessons (id INTEGER PRIMARY KEY, name TEXT NOT NULL, progress INTEGER NOT NULL, module_id INTEGER NOT NULL, FOREIGN KEY (module_id) REFERENCES module (id))"""
        )
        self.conn_us.commit()
        self.conn_mod.commit()
        self.conn_less.commit()

    def db_add_users(self, id=1, name=None, brain=0):
        self.conn_us.execute(f"INSERT INTO users (id, name, brain) VALUES ({id}, '{name}', {brain})")

    def db_add_mod(self, id=1, name=None, progress=0, lessons_count=0):
        self.conn_mod.execute(f"""INSERT INTO module (id, name, progress, lessons_count) VALUES ({id}, '{name}', {progress}, {lessons_count})""")

    def db_add_less(self, id=1, name=None, progress=0, mod_id=1):
        self.conn_less.execute(f"""INSERT INTO lessons (id, name, progress, module_id) VALUES ({id}, '{name}', {progress}, {mod_id})""")

    def us_base_get(self, col_name: str):
        return self.conn_us.execute(f"""SELECT {col_name} FROM users""")

    def mod_base_get(self, col_name: str):
        return self.conn_mod.execute(f"""SELECT {col_name} FROM module""")

    def less_base_get(self, col_name: str):
        return self.conn_less(f"""SELECT {col_name} FROM lessons""")
