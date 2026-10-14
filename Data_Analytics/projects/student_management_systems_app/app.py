import matplotlib.pyplot as plt 
import numpy as np 
import openpyxl
import sqlite3
import pandas as pd
# made connection 
conn=sqlite3.connect("student_management_db")
# print("database created successfully")
# create table schema 
cur=conn.cursor()
# create country table 
cur.execute(
    """ 
    create table if not exists country(
        cid integer primary key autoincrement,
        cname text
    )
    """
)

# create state table 
cur.execute(
    """ 
    create table if not exists state(
        sid integer primary key autoincrement,
        sname text
    )
    """
)

# create city table 
cur.execute(
    """ 
    create table if not exists city(
        ctid integer primary key autoincrement,
        ctname text
    )
    """
)

# create departemnt table 
cur.execute(
    """ 
    create table if not exists department(
        depid integer primary key autoincrement,
        depname text
    )
    """
)

# create college table 
cur.execute(
    """ 
    create table if not exists college(
        collegeid integer primary key autoincrement,
        collegename text
    )
    """
)

# create faculty table 
cur.execute(
    """ 
    create table if not exists faculty(
        fid integer primary key autoincrement,
        fname text,
        fmobile integer,
        faddress text
    )
    """
)


# create students table 
cur.execute(
    """ 
    create table if not exists students(
        stdid integer primary key autoincrement,
        stdname text,
        stdmobile integer,
        stdaddress text,
        stddescriptions text,
        
        cid INTEGER,
        sid INTEGER,
        ctid INTEGER,
        depid INTEGER,
        collegeid INTEGER,
        fid INTEGER,
        
        foreign key(cid) references country(cid),
        foreign key(sid) references state(sid),
        foreign key(ctid) references city(cid),
        foreign key(depid) references department(depid),
        foreign key(collegeid) references college(collegeid),
        foreign key(fid) references faculty(fid)
    )
    """
)


# insert data in country tables 
insCountry=[
        (1,'india'),
        (2,'usa'),
        (3,'canada'),
        (4,'australia'),
        (5,'erope'),
        (6,'china')
    ]
cur.executemany(  
    """
    insert or replace into country values(?,?)
    """,insCountry)

# insert data in state tables 
insState=[
        (1,'gujrat'),
        (2,'uttar pradesh'),
        (3,'Madhya Pradesh'),
        (4,'California'),
        (5,'Alasca'),
        (6,'Sanghai')
    ]
cur.executemany(  
    """
    insert or replace into state values(?,?)
    """,insState)

# insert data in city tables 
insCity=[
        (1,'Rajkot'),
        (2,'Ahemdabad'),
        (3,'Surat'),
        (4,'Junagad'),
        (5,'Lucknow'),
        (6,'Varansi')
    ]
cur.executemany(  
    """
    insert or replace into city values(?,?)
    """,insCity)


# insert data in department tables 
insDep=[
        (1,'IT'),
        (2,'CSE'),
        (3,'EC'),
        (4,'MBA'),
        (5,'Data science'),
        (6,'Data analytics')
    ]
cur.executemany(  
    """
    insert or replace into department values(?,?)
    """,insDep)



# insert data in department tables 
insCollege=[
        (1,'Marawadi Univercity'),
        (2,'Atmiya Univercity'),
        (3,'Darshan Univercity'),
        (4,'Govt Engineering college'),
        (5,'Govt Mahila College'),
        (6,'Govt polytechnic college')
    ]
cur.executemany(  
    """
    insert or replace into college values(?,?)
    """,insCollege)


# insert data in faculty tables 
insFaculty=[
        (1,'Dr sadanand patel',9998003879,'150 feet ring road rajkot'),
        (2,'Dr Mishri Patel',9998003889,'50 feet ring road surat'),
        (3,'Prof. chinmay dongra',654587854,'navada near CA california usa')
    ]
cur.executemany(  
    """
    insert or replace into faculty values(?,?,?,?)
    """,insFaculty)



# insert data in faculty tables 
insStudents=[
        (1,'faig',9978073879,'50 feet ring road rajkot','Good students with A grade',1,1,1,2,1,2),
        (2,'meet',7978073879,'50 feet ring road rajkot','Good students with A grade',3,2,2,2,2,3),
        (3,'pranav',6978073879,'50 feet ring road rajkot','Good students with A grade',2,2,1,2,1,1),
        (4,'forum',6478073879,'50 feet ring road rajkot','Good students with A grade',2,2,1,3,1,2),
        (5,'brijesh',6378073879,'50 feet ring road rajkot','Good students with A grade',2,2,1,1,1,3)
        
    ]
cur.executemany(  
    """
    insert or replace into students values(?,?,?,?,?,?,?,?,?,?,?)
    """,insStudents)


# display all students data from students tables with join another tables also to display all students informations
query="select students.*,cname,sname,ctname,depname,collegename,fname from students join country on students.cid=country.cid join state on students.sid=state.sid join city on students.ctid=city.ctid join department on students.depid=department.depid join college on students.collegeid=college.collegeid join faculty on students.fid=faculty.fid"


df = pd.read_sql_query(query, conn)
print("-" * 60)
print("All students data fetched successfully!")
print(df.to_string(index=False))
print("Total students:", len(df))


with pd.ExcelWriter("students_department_wise.xlsx",
                    engine="openpyxl") as writer:

    # All students
    df.to_excel(
        writer,
        sheet_name="All Students",
        index=False
    )

    # Department-wise summary
    summary = (
        df.groupby("depname", dropna=False)
        .size()
        .reset_index(name="Total Students")
    )

    summary.to_excel(
        writer,
        sheet_name="Department Summary",
        index=False
    )

    # Separate Excel sheet for each department
    for department, data in df.groupby(
        "depname", dropna=False
    ):
        sheet_name = str(department or "Unknown")[:31]
        data.to_excel(
            writer,
            sheet_name=sheet_name,
            index=False
        )

print("Excel file created successfully!")


# Count students in each department
department_count = df["depname"].fillna("Unknown").value_counts()
# Create pie chart
plt.figure(figsize=(9, 7))
plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Students Distribution by Department")
plt.axis("equal")
plt.show()



# print messages
# print("tables created successfully")
# save query
conn.commit()
conn.close()
