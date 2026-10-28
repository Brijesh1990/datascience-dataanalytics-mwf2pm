import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
import seaborn  as snb
import openpyxl
import mysql.connector
from mysql.connector import Error
# create a database connection 
try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="task_manager_db_app"    
    )
    if conn.is_connected():
        # print("connection established successfully")
        cursor=conn.cursor()
        # create a table inside of database 
        cursor.execute("""
                     CREATE TABLE IF NOT EXISTS assignto (
                     userid INT PRIMARY KEY AUTO_INCREMENT,
                     name VARCHAR(100),
                     age INT,
                     mobile VARCHAR(15),
                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                  )               
                   
                   """)
        
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS task (
                    taskid INT PRIMARY KEY AUTO_INCREMENT,
                    title VARCHAR(100),
                    created_date varchar(255),
                    userid int,
                    foreign key(userid) references assignto(userid),
                    status enum('pending','completed'),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )               
                
                """)
        print('table successsfully created')
        # saved query
        conn.commit()
        # closed connection
        conn.close()
except Error as e:
    print('something went wrong please check {e}') 
