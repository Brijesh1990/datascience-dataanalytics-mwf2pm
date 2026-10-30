import matplotlib.pyplot as plt
import pandas as pd
import seaborn as snb
import numpy as np
import openpyxl
import mysql.connector
from mysql.connector import Error


# # create a databse connection with mysql
# try:

#     conn=mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         port=3306,
#         password="",
#         database="sales_db_app",
#         )
       
#     if conn.is_connected():
#         print("database is connected")


# except Error as e:
#     print("databse is not connected")
# print('brijesh')
# print('brijesh')

conn=mysql.connector.connect(
        host="localhost",
        user="root",
        port=3306,
        password="admin",
        database="sales_db_app"
)
cursor=conn.cursor()
print('database connected successfully')