# create a database connection 
import pandas as pd
import numpy as np
import matplotlib as plt
import openpyxl as xl
import sqlite3
# connect database 
conn=sqlite3.connect("task_manager_app_db")
# create a crud app of employee management systems
# insert data using sqlite3 in task_manager_app_db and insert or add multiple employee in employee tables 
cur=conn.cursor()
insert=[
    (1,"meet","meet007@gmail.com",9998003879,"18500","IT","150 feet ring road rajkot","09-10-2026"),
    
    (2,"faig","faig007@gmail.com",9998003779,"19500","IT","150 feet ring road rajkot","09-10-2026"),
    
    (3,"forum","forum007@gmail.com",9998003579,"20500","CSE","150 feet ring road rajkot","02-10-2026"),
    
    (4,"pranav","pranav007@gmail.com",9998003479,"21500","EC","150 feet ring road rajkot","08-10-2026"),
    
    (5,"mishri","mishri@gmail.com",9998003379,"22500","HR","150 feet ring road rajkot","07-10-2026"),
    
    (6,"brijesh","brijesh007@gmail.com",9998003279,"23500","IT","150 feet ring road rajkot","06-10-2026"),
    
    (7,"om","om007@gmail.com",9998003179,"25500","CSE","150 feet ring road rajkot","05-10-2026"),
    
    
    (8,"kumar","kumar007@gmail.com",6858003179,"25500","CSE","150 feet ring road rajkot","01-10-2026"),
    
    (9,"rupesh","rupesh007@gmail.com",7858003179,"25500","CSE","150 feet ring road rajkot","01-10-2026"),
]

# query execute 

cur.executemany(
    """ 
    insert or replace into employee values(?,?,?,?,?,?,?,?)
    
    """, insert)

# save query in database 
conn.commit()
print("Employee added successfully")


# display all employee data from employee tables or fetch or retrieve employee data
query="select * from employee"
df=pd.read_sql(query, conn)
print('-----------------------------------------------------------')
print("Data fetch successfully \n",df)

print('-------------------------------------------------------------')
# find the highest salary 
highest_salary=df["salary"].max()
print("Find Highest salary :",highest_salary)


print('-------------------------------------------------------------')
# find the minimum salary 
minimum_salary=df["salary"].min()
print("Find Minimum salary :",minimum_salary)

print('-------------------------------------------------------------')

# find the Total salary 
total_salary=df["salary"].sum()
print("Total sum of salary :",total_salary)


print('-------------------------------------------------------------')

# find the Total average salary 
avg_salary=df["salary"].mean()
print("Total average of salary :",avg_salary)


# close the connection
conn.close()



