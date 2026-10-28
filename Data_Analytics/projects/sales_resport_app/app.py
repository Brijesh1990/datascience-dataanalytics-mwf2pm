import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as snb
import numpy as np 
import openpyxl
import mysql.connector
from mysql.connector import Error

# create a database connection with mysql
# try:
#     conn=mysql.connector.connect(
#         # host="localhost"
#         host="127.0.0.1",
#         user="root",
#         port=3306, 
#         password="admin",
#         database="sales_db_app"    
#     )
#     if conn.is_connected():
#         print("database connected successfully")
    
# except Error as e:
#     print("Database is not conected something went wrong")  

conn=mysql.connector.connect(
        # host="localhost"
        host="127.0.0.1",
        user="root",
        port=3306, 
        password="admin",
        database="sales_db_app"    
    )
if conn.is_connected():
    cursor=conn.cursor()
    print("database connected successfully")
    
# create a tables structured inside of database 
# create table country
cursor.execute("""
               
               create table if not exists tbl_country(
                   cid int primary key auto_increment,
                   cname varchar(255),
                   created_at varchar(200)
               )
               
               """)

# create table state
cursor.execute("""
               
               create table if not exists tbl_state(
                   sid int primary key auto_increment,
                   sname varchar(255),
                   cid int,
                   foreign key(cid) references tbl_country(cid),
                   created_at varchar(200)
               )
               
               """)

# create table city
cursor.execute("""
               
               create table if not exists tbl_city(
                   ctid int primary key auto_increment,
                   ctname varchar(255),
                   sid int,
                   foreign key(sid) references tbl_state(sid),
                   created_at varchar(200)
               )
               
               """)
conn.commit()
print('table creatd successfully')
conn.close()
    
