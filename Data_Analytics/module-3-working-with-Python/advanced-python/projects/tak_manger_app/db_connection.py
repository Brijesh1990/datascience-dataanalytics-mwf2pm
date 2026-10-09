# import sqllite3
import sqlite3
# create a database 
conn=sqlite3.connect("task_manager_app_db")
print("Database created successfully")
conn.close()