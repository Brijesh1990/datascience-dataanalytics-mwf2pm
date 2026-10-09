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

# cur=conn.cursor()
# cur.execute(
#     """
#     create table if not exists feedback(
#      fid integer primary key autoincrement,
#      name text,
#      email text,
#      mobile text,
#      comment text,
#      created_date text
#     )
    
#     """
# )


cur=conn.cursor()
cur.execute(
    """
    create table if not exists employee(
     empid integer primary key autoincrement,
     name text,
     email text,
     mobile integer,
     salary integer,
     department text,
     address text,
     created_date text
    )
    
    """
)

# print mesages 
print("Table created successfully in database")

#drop table employee 

# cur=conn.cursor()
# cur.execute(
#     """
#     drop table employee
#     """
# )

# save query
conn.commit()
# print("table deleted successfully")
conn.close()