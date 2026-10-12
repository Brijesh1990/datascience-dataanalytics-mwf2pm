# create a data frames 
import pandas as pd 
import matplotlib.pyplot as plt 
import openpyxl
import sqlite3

# dataframes
# data = {
#     "studentname": ["Faiz", "Jay", "Meet", "forum", "rutwick", "brijesh"],
#     "attendance": [0, 0, 1, 1, 1, 1]
# }

# Create DataFrame
# df = pd.DataFrame(data)

# sqlite3 connections
# connect database 
conn=sqlite3.connect("attendance_manage_db")
# create a crud app of students attendance 
# insert data using sqlite3 in attendance_manage_db and insert or add  attendance in attendance tables 

# create a attendance tables 
cur=conn.cursor()
# create tables 
cur.execute("""
    create table if not exists attendance(
     id integer primary key autoincrement,
     name text,
     att_col integer
     )
     """)

# add attendance

insert=[
    (1,"meet",1),
    (2,"faif",0),
    (3,"mishri",0),
    (4,"forum",0),
    (5,"pranav",1),
    (6,"astha",1),
    (7,"kumar",1),
    (8,"smit",1),
    (9,"lokesh",0),
    (10,"sneha",1),
    (11,"brijesh",0)
    
]

# query execute 
cur.executemany(
    """ 
    insert or replace into attendance values(?,?,?)
    """,insert)


# fetch data from tables 
query="select * from attendance"
df=pd.read_sql(query, conn)
print('-----------------------------------------------------------')
print("Data fetch successfully \n",df)

# save query in database 
conn.commit()
print("attendance added successfully")


# generate data in excel 
generate_data_excel=df.to_excel('students.xlsx', engine="openpyxl",index=False)
print("Excel files generated successfully",generate_data_excel);



# Count present and absent students

present = (df["att_col"] == 1).sum()
absent = (df["att_col"] == 0).sum()

# Data for pie chart
labels = ["Present", "Absent"]
values = [present, absent]
colors = ["green", "red"]

# Create pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    values,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Attendance Management System")
plt.show()


# Display counts
print("Present Students:", present)
print("Absent Students:", absent)
