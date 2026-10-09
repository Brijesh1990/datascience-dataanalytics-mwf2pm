 **faculty based database**

1. create a database named "university"

2. create a table named "faculty" with the following columns: faculty_id (primary key), faculty_name, department, and country_id (foreign key referencing the country table) and provides email as unique key in faculty tables.

3. insert at least 5 records into the faculty table.

4. create a table named "courses" with the following columns: course_id (primary key), course_name, and faculty_id (foreign key referencing the faculty table).

5. insert at least 3 records into the courses table.  

6. create a table named "students" with the following columns: student_id (primary key), student_name, age, and country_id (foreign key referencing the country table).

7. insert at least 5 records into the students table.

8. create a table named "enrollments" with the following columns: enrollment_id (primary key), student_id (foreign key referencing the students table), course_id (foreign key referencing the courses table), and enrollment_date.

9. insert at least 5 records into the enrollments table.


10. write a query to select all enrollments along with student names and course names.

11. write a query to find the total number of students enrolled in each course.

12. write a query to find the faculty member teaching the most courses.

13. write a query to update the department of a faculty member with a specific faculty_id.

14. write a query to delete a student with a specific student_id.

**Note: after creating database and tables you will insert some data in that tables then you will apply all the queries on that data to understand better**