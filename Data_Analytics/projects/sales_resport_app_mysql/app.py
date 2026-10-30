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



# create table users
cursor.execute("""
               create table if not exists tbl_users(
                   uid int primary key auto_increment,
                   uname varchar(255),
                   age int,
                   salary int, 
                   company varchar(255),
                   address text,
                   
                   cid int,
                   sid int,
                   ctid int,
                   
                   foreign key(cid) references tbl_country(cid),
                   
                   foreign key(sid) references tbl_state(sid),
                                      
                   foreign key(ctid) references tbl_city(ctid),
                   created_at varchar(200)
               )
               
               """)


# create a choice based to add data in tables 
# add country in tables 
print("========select 1 : add country")
print("========select 2 : add state")
print("========select 3 : add city")
print("========select 4 : add users")
print("========select 5 : fetch all users Data")
print("========select 6 : fetch max salary data")
print("========select 7 : Generate data in excels")
print("========select 8 : terminate programmes")

while True: 
    choice=int(input("Enter your choice :"))
    if choice==1:
        cname=input("Enter country Name :")
        created_at=input("Enter your added Date  :")

        data=(cname,created_at)
        cur=conn.cursor()
        cur.execute("""
                    
                    insert into tbl_country(cname,created_at) values(%s,%s)
                    """,data)
        conn.commit()
        print("country added successfully")
    elif choice==2:
            sname=input("Enter state Name :")
            cid=int(input("Enter cid here : "))
            created_at=input("Enter your added Date  :")
    
            data=(sname,cid,created_at)
            cur=conn.cursor()
            cur.execute("""
                        
                        insert into tbl_state(sname,cid,created_at) values(%s,%s,%s)
                        """,data)
            conn.commit()
            print("state added successfully")
        
    elif choice==3:
                    ctname=input("Enter city Name :")
                    sid=int(input("Enter sid here : "))
                    created_at=input("Enter your added Date  :")
            
                    data=(ctname,sid,created_at)
                    cur=conn.cursor()
                    cur.execute("""
                                
                                insert into tbl_city(ctname,sid,created_at) values(%s,%s,%s)
                                """,data)
                    conn.commit()
                    print("city added successfully")
                    
    elif choice==4:
                    uname=input("Enter User Name :")
                    age=int(input("Enter your age  :"))
                    salary=int(input("Enter your salary :"))
                    company=input("Enter your company  :")
                    address=input("Enter your Address  :")
                                        
                    cid=int(input("Enter cid here : "))
                    sid=int(input("Enter sid here : "))
                    ctid=int(input("Enter ctid here : "))
                                                            
                    created_at=input("Enter your added Date  :")
               
                    data=(uname,age,salary,company,address,cid,sid,ctid,created_at)
                    cur=conn.cursor()
                    cur.execute("""
                                   
                                   insert into tbl_users(uname,age,salary,company,address,cid,sid,ctid,created_at) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                   """,data)
                    conn.commit()
                    print("Users added successfully")
    elif choice==5:
        
        # select="select * from tbl_users"
        # df=pd.read_sql(select,conn)
        # print(df)
        
        select="select tbl_users.*,cname,sname,ctname  from tbl_users join tbl_country on tbl_users.cid=tbl_country.cid  join tbl_state on tbl_users.sid=tbl_state.sid  join tbl_city on tbl_users.ctid=tbl_city.ctid"
        df=pd.read_sql(select,conn)
        print(df)
        
    elif choice==6:
        select="select max(salary) as maximum_salary from tbl_users"
        df=pd.read_sql(select,conn)
        print("max salary is :",df)
    
    elif choice==7:
            
             select="select * from tbl_users"
             df=pd.read_sql(select,conn)
             excel_generate=df.to_excel("users_data.xlsx", engine='openpyxl', index=False)
             print("Excels generated successfully",excel_generate)
       
    else:
        print("Programmes exist here")
        break
                

conn.commit()
# print('table created successfully')
conn.close()
    
