from decouple import config

from .entities.users import User
from database.factory import Factory
from database.db import DataBase
from database.my_sql import MySQL
from database.postgres import Postgres

factory = Factory()
datab = factory.connect(config('DATABASE_ADAPTER'))

class UserModel():

    @classmethod
    def get_users(self):    
        try:
            connection = datab.get_connection()
            users=[]

            with connection.cursor() as cursor:

                cursor.execute("SELECT * FROM users")
                resultset = cursor.fetchall()

                for row in resultset:
                    user=User(row[0], row[1], row[2], row[3])
                    users.append(user.to_JSON())
            
            connection.close()
            return users

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id):   
        try:
            connection = datab.get_connection()

            with connection.cursor() as cursor:

                cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
                row = cursor.fetchone()

                user=None

                if row != None:
                    user=User(row[0], row[1], row[2], row[3])
                    user=user.to_JSON()
            
            connection.close()
            return user

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_user(self, user):       
        try:
            connection = datab.get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO users(id, name, password, cell) 
                                    VALUES (%s, %s, %s, %s)""", (user.id, user.name, user.password, user.cell))

                affected_row=cursor.rowcount

                connection.commit() 

            connection.close()
            return affected_row

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_user(self, user):       
        try:
            connection = datab.get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id = %s", (user.id,))

                affected_row=cursor.rowcount
                connection.commit() 

            connection.close()
            return affected_row

        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def update_user(self, user):       
        try:
            connection = datab.get_connection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE users SET name = %s, password = %s, cell = %s WHERE id = %s", (user.name, user.password, user.cell, user.id))

                affected_row=cursor.rowcount
                connection.commit() 

            connection.close()
            return affected_row

        except Exception as ex:
            raise Exception(ex)