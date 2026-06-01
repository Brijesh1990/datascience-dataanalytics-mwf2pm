# what is SQL  ?

  1. SQL stands for structured query language
  2. SQL case insenstive language
     examples : INSERT or insert or Insert
  3. sql is used to create an structured of tables or database  
  4. sql is used to create database or tables and manupulate data 
  5. SQL create structures or manipulate data in table 
  6. SQL is maximum create 1032 columns 
  7. SQL is faster to create structured data or insert data or delete data or update data 
 

# employee details table with columnname id, name , email , address , mobile etc

**employee**

| ID  | Name           | Email                     | Phone        | Address                     | Salary |
|-----|----------------|---------------------------|--------------|-----------------------------|--------|
| 101 | John Doe       | john.doe@example.com      | 9876543210   | 12 Main St, New York        | 55000  |
| 102 | Sarah Smith    | sarah.smith@example.com   | 9123456780   | 45 Oak Ave, Chicago         | 62000  |
| 103 | Michael Brown  | michael.brown@example.com | 9988776655   | 78 Pine Rd, California      | 58000  |
| 104 | Emily Johnson  | emily.johnson@example.com | 9012345678   | 23 Lake View, Texas         | 64000  |
| 105 | David Wilson   | david.wilson@example.com  | 9090909090   | 56 Hill St, Florida         | 60000  |


# types of  SQL query or commands

  1. DDL (data definition language)
  2. DML (data manipulate language)
  3. DQL (data query language)
  4. TCL (transanctional query language)


# what is DDL ....  Data definition language

  1. stands for data definition language 
  2. DDL used to create database and table structures 
  3. DDL is also used to drop & alter the database structures and tables data

  **List of command or query in DDL**

  1. create (create database or tables structures)
  2. alter  (alter used to add | modify  | rename  new  column after create tables)
  3. drop
  4. rename
  5. change 
  6. truncate

  **How to create database**

  ```
  syntax ..
  create database databasename
  examples : 
  create database data_analytics
  ```  

  **How to create a table**
  
  **create columnname in tables fixed data-type**

  1. char .....accept character values size(0-255)
  2. varchar .....accept character and numbers both values size(0-255)
  3. int..........accept numbers only default size(0-11)
  4. bigint ......accept more than 11 number default size(0-20)
  5. text.........accept more than 65365 character  
  6. enum .........enumerated accept multiple choices values
  7. date...........accept date formate 
  8. datatime........accept datetime both
  9. float...........accept decimal values 
  10. money..........accept price & all   
  
 **syntax to create table** 

  ```
  create table tablename
  (
  columnname datatype(size) primary key auto_increment,
  columname datatype(size),
  .
  .
  .
  .
  .
  columnname datatype(size)

  );

  ```
  
  **examples of create table***

  ```
  create table employee
(
empid int primary key AUTO_INCREMENT,
name varchar(100),
email varchar(255),
password varchar(255),
address text,
phone bigint,
picode int,
salary float    
)

```

```
create table country
(
cid int primary key AUTO_INCREMENT,
countryname varchar(255),
added_date varchar(255)    

)

```

```
create table feedback
(
id int primary key AUTO_INCREMENT,
name varchar(255),
email varchar(255),
phone bigint,
rating varchar(255),
comment text,
added_date date    
)

```


 **alter**

1. alter : (alter used to add | modify  | rename | drop  a   column after create tables)

```
add new column...

1. alter table employee add added_date date;
2. alter table employee add country varchar(155);
3. alter table employee add photo varchar(255) after empid;

rename any columns 

1. alter table employee change salary employee_salary varchar(255);
2. alter table employee change photo employee_image varchar(255);

delete any columns 

1. alter table employee drop added_date;

```

**drop database & table structured**

```
delete a database and table structured after drop we can not rollback

```

**drop database**

```

drop database databasename
or
drop database data_analytics

```

**drop table only**

```
drop a table it is drop or delete permanently after drop we can not rollback a data or structured of table

drop table tablename
or
drop table country

```

**truncate**

```
truncate delete data or cleared data from table 
after truncate we can not rollback or undo the data 
after truncate it cleared all data 
truncate can not effects on structured its only delete data

syntax ..
truncate table tablename
or
truncate table reviews

```

**rename**

```
rename is used to rename the table
syntax :
rename table tablename to newtablename
or
rename table employee to tbl_employee
or
rename table reviews to tbl_reviews
```


**change**

```
change is used to change any columname in table 
syntax :
alter table tablename change columnname newcolumnname datatype(size);
or
alter table tbl_employee change password employee_password varchar(255);
```



# what is DML ....  Data manipulation language

  1. stands for data manipulation language 
  2. DML used to manipulate data meanse insert | delete | update data in tables 
  3. DML data 

     a. insert 
     b. delete 
     c. update 

**how to insert a single or multiple data in tables**

1. insert a single row in table

   ```
   syntax :

   insert into tablename(columnname1, columnname2) values ('value1','value2');
   or

   insert into tbl_reviews(name,email,phone,rating,comment,added_date) values ('om','om@gmail.com',91212121,'5 star','good i am glad to here','19-05-2026') 

   ```


   2. insert a multiple rows in table

   ```
   syntax :

   insert into tablename(columnname1, columnname2) values ('value1','value2'),('value1','value2'),('value1','value2');
   or
   
   insert into tbl_reviews(name,email,phone,rating,comment,added_date) values ('amish','amish@gmail.com',91212178,'5 star','good i am glad to here','2026-05-19'),('kirtan','kirtan@gmail.com',93212178,'5 star','good i am glad to here','2026-05-19'),('mahesh','mahesh@gmail.com',95212178,'5 star','good i am glad to here','2026-05-19') 

   or

  insert into tbl_reviews values('null','naimish','naimish@gmail.com',91212178,'5 star','good i am glad to here','2026-05-19'),('null','ritesh','ritesh@gmail.com',93212178,'5 star','good i am glad to here','2026-05-19'),('null','kumar','kumar@gmail.com',95212178,'5 star','good i am glad to here','2026-05-19')

   ```

# how to delete data 

  1. delete data is used to delete a data 
  2. delete is also used to delete a particular one rows 
  3. delete is also used to delete with its columnname 
  4. delete is also used to delete a range of data 
  5. delete is also used to delete alternate data 

 **examples of delete**

  ```
  delete from tablename
  or 
  delete from tbl_reviews
  or 
  delete from tbl_reviews where id=5;
  or
  delete from tbl_reviews where name='om';
  or
  delete from tbl_reviews where id between 5 and 10;
  or
  delete from tbl_reviews where id in(12,14,16,19)
  ```   

# how to delete data or rows 

  1. update a rows ...

  ```
   update tablename set colunname='value' where id;
   or
   update tbl_reviews set name='om',email='om007@gmail.com',phone=635898956,rating='5star',comment='good to see you',added_date='2026-05-21' where id=17;
   or
   update tbl_reviews set name='om',email='om007@gmail.com',phone=635898956,rating='5star',comment='good to see you',added_date='2026-05-21' where id=17;

   or

   update tbl_reviews set email='bkpandey.pandey@gmail.com' where id=1;

   or

   update tbl_reviews set email='bkpandey.pandey@gmail.com' where id=1;

   or

   update tbl_reviews set email='mukeshdhandhukiya007@gmail.com' where name='mukesh';   

  ```
  # DQL ..stands for data query language 

  1. DQL stands data query language 
  2. DQL is used to select or fetch data 
  3. DQL is only used select query or command

  **select examples**

  ```
  select * from tbl_reviews;
  or
  select * from tbl_reviews id=1;
  or
  select * from tbl_reviews where id=1;
  or
  select * from tbl_reviews where between 18 and 25;
  or
  select * from tbl_reviews where id in(13,17,20);
  or
  select id,name,email,phone from tbl_reviews;
  or
  select * from tbl_reviews where id limit 1,6;
  or
  select * from tbl_reviews order by name asc
  or
  select * from tbl_reviews order by name desc
  
  ```

# SQL function ....

 1. SQL function provides a group of code 
 2. SQL function is inbuilt function 
 3. SQL function is used to completed any task 

# types of SQL function 

  1. aggrigate function
  2. scalar function 

# aggrigate function 
  1. sum 
  2. avg 
  3. count 
  4. max
  5. min

# scalar function 
  1. first 
  2. last 
  3. ucase
  4. lcase


# sum() : sum used to sum of values 
   
   **syntax**

   ```
   select sum(employee_salary) as sumof_salary from tbl_employee
   ```

# alias : alias is a nick name of any column name     

   ```
    select employee_password as password from tbl_employee
   ```

# avg() : avg used to calculate average values  
   
   **syntax**

   ```
   select avg(employee_salary) as averageofsalary from tbl_employee
   ```

# count() : count used to calculate a count values   
   
   **syntax**

   ```
   select count(empid) as totalnumberemployee from tbl_employee
   or 
   select count(id) as totalreviews from tbl_reviews
   ```
# max() : max used to calculate a max values   
   
   **syntax**

   ```
  select max(employee_salary) as max_salary from tbl_employee

   ```

# min() : min used to calculate a min values   
   
   **syntax**

   ```
   
  select min(employee_salary) as min_salary from tbl_employee

   ```

# subquery : subquery used a query within another query i.e called subquery 

 1. find a second highest salary from tables 

 ```
   select max(employee_salary) from tbl_employee where employee_salary < (select max(employee_salary) from tbl_employee);
   
   or

   select max(employee_salary) as second_highest_salary from tbl_employee where employee_salary < (select max(employee_salary) from tbl_employee); 
 ```

# first :find the first rows of data 
 **select first rows**
 ```
  select first(id) from tbl_reviews
 ```  

# last: find the last rows of data

   **select last rows**
   ```
  select last(id) from tbl_reviews
  
  ```

# ucase :convert any columnname of data in uppercase 

  **convert in uppercase**

  ```
  select ucase(name) from tbl_reviews
  or

  ```

# lcase :convert any column name of data in lowercase 

 **convert in lowercase**

  ```
  select lcase(name) from tbl_reviews
  ```
# like operator : searching rows or data from tables using like operator

1. searching data from tables using keyword like operator is used
2. like operator is denoted by % symbol 
3. like is used to search via character word pattern 

```
select * from tbl_reviews where name like 'r%';
select * from tbl_reviews where name like 'n%';
select * from tbl_reviews where name like '%h';
select * from tbl_reviews where name like '%a%';
select * from tbl_reviews where name like 'a%h';
```

# pattern word rules in like operator

| Pattern | Meaning | Example Match |
|---|---|---|
| `'a%'` | Starts with "a" | `"apple"`, `"alpha"` |
| `'%a'` | Ends with "a" | `"banana"`, `"data"` |
| `'%or%'` | Contains "or" in any position | `"world"`, `"orbit"` |
| `'_r%'` | Has "r" in the second position | `"tree"`, `"area"` |
| `'a__%'` | Starts with "a" and is at least 3 chars long | `"apple"`, `"and"` |
| `'a%o'` | Starts with "a" and ends with "o" | `"audio"`, `"alto"` |



# key constraints in SQL ........

1. key constraints in SQL ...
2. key constraints in SQL set limit on tables 
3. key constraints is ........

   1. primary key 
   2. unique key 
   3. foreign key 


**note:key constraints is also used to normalized tables data**    
