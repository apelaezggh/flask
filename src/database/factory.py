import psycopg2
from psycopg2 import DatabaseError
from decouple import config

from .my_sql import MySQL
from .postgres import Postgres

class Factory():

    def connect(self, db):
        if db == 'postgres':
            return Postgres()
        elif db == 'mysql':
            return MySQL()
        else:
            print("BD empty")
