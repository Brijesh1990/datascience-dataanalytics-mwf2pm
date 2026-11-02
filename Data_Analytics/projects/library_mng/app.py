import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="library_mng_db"
)

print("Connected to the database successfully!")


cur=conn.cursor()


cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                published_year INT
            )
        """)


conn.commit()
print("Table created successfully!")

while True:
  print("1. Insert data")
  print("2. Export data to Excel")
  print("3. Create chart")
  choice=int(input("Enter your choice (1, 2, or 3): "))
  
  if choice==1:
      
      #insert data via input
    title=input("Enter the book title: ")
    author=input("Enter the book author: ")
    published_year=int(input("Enter the published year: "))

    query="""INSERT INTO books (title, author, published_year) VALUES (%s, %s, %s)"""
    values=(title, author, published_year)

    cur.execute(query, values)
    conn.commit()
    print("Data inserted successfully!")
 
  elif choice==2:
      df=pd.read_sql("SELECT * FROM books", conn)
      print(df)
       
      excel_file=df.to_excel("books_data.xlsx", index=False, engine='openpyxl')
     
      print("Excel file created successfully")
  elif choice==3:
      
      
       df=pd.read_sql("SELECT * FROM books", conn)
       plt.bar(df['title'], df['published_year'])
       plt.xlabel('Book Title')
       plt.ylabel('Published Year')
       plt.title('Book Publication Years')
       plt.show()
  else:
          print("Invalid choice. Please try again.")
 
 