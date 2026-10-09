import mysql.connector 
from mysql.connector import Error
#create a function for database connection
def create_connection():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="myapp_db"
        )
        if connection.is_connected():
            print("database successfully connected")
            return connection
    except Error as e:
        print("connection not successfully stablished",e)