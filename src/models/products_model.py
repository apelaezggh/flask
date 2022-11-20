from decouple import config

from .entities.product import Product
from database.factory import Factory
from database.db import DataBase
from database.my_sql import MySQL
from database.postgres import Postgres

factory = Factory()
datab = factory.connect(config('DATABASE_ADAPTER'))

class ProductModel():

    @classmethod
    def get_products(self): 
      
        try:
            connection = datab.get_connection()
            products=[]

            with connection.cursor() as cursor:

                cursor.execute("SELECT * FROM products")
                resultset = cursor.fetchall()

                for row in resultset:
                    product=Product(row[0], row[1], row[2])
                    products.append(product.to_JSON())
            
            connection.close()
            return products

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_product(self, id):   
        try:
            connection = datab.get_connection()

            with connection.cursor() as cursor:

                cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
                row = cursor.fetchone()

                product=None

                if row != None:
                    product=Product(row[0], row[1], row[2])
                    product=product.to_JSON()
            
            connection.close()
            return product

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_product(self, product):       
        try:
            connection = datab.get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO products(id, name, unit_measure) 
                                    VALUES (%s, %s, %s)""", (product.id, product.name, product.unit_measure))

                affected_row=cursor.rowcount

                connection.commit() 

            connection.close()
            return affected_row

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_product(self, product):       
        try:
            connection = datab.get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM products WHERE id = %s", (product.id,))

                affected_row=cursor.rowcount
                connection.commit() 

            connection.close()
            return affected_row

        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def update_product(self, product):       
        try:
            connection = datab.get_connection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE products SET name = %s, unit_measure = %s WHERE id = %s", (product.name, product.unit_measure, product.id))

                affected_row=cursor.rowcount
                connection.commit() 

            connection.close()
            return affected_row

        except Exception as ex:
            raise Exception(ex)