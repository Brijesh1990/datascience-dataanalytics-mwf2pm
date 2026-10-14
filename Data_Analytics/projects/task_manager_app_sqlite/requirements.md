# create task manager app using sqllite database 

1. install all dependencies 
2. pip install pandas numpy openpyxl matplotlib 
3. create some python file for perform **crud** operation

# what is crud operation ? 

  **C** : create 
  **r** : read 
  **u** : update 
  **d** : delete 

# create a database connection and table via sqllite

**create datebase**

```
# import sqllite3
import sqlite3
# create a database 
conn=sqlite3.connect("task_manager_app_db")
print("Database created successfully")
conn.close()
```


**create a table in database**

```
# create a table via sqlite3 in task_manager_app_db
import sqlite3
# create database connection 
conn=sqlite3.connect("task_manager_app_db")

# create a tables in database name of tasks
# cur=conn.cursor()
# cur.execute(
#     """
#     create table if not exists tasks(
#      id integer primary key autoincrement,
#      title text,
#      assign_date text,
#      status text,
#      comment text
#     )
    
#     """
# )

# create a table in database with name of users
# cur=conn.cursor()
# cur.execute(
#     """
#     create table if not exists users(
#      uid integer primary key autoincrement,
#      name text,
#      email text,
#      mobile text,
#      address text
#      gender text,
#      hobby text,
#      created_date text
#     )
    
#     """
# )

cur=conn.cursor()
cur.execute(
    """
    create table if not exists feedback(
     fid integer primary key autoincrement,
     name text,
     email text,
     mobile text,
     comment text,
     created_date text
    )   
    """
)
# print mesages 
print("Table created successfully in database")
# save query
conn.commit()
conn.close()
```
