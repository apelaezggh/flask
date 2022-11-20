import psycopg2
from psycopg2 import DatabaseError
from decouple import config
import mysql.connector

from .db import DataBase

class MySQL(DataBase):

    def get_connection(self):
        print("connecting mysql...")
        try:
            return mysql.connector.connect(
                host=config('MYSQL_HOST'),
                user=config('MYSQL_USER'),
                password=config('MYSQL_PASSWORD'),
                database=config('MYSQL_DB')
            )
        except DatabaseError as ex:
            raise ex
