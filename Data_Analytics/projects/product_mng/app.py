import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect('data.db')

print("Connected to the database successfully.")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        quantity INTEGER ,
        price REAL,
        supplier TEXT
    )''')

print("Table created successfully.")

# insert data into the table

while True:

    print("press 1 to add data")
    print("press 2 to excel sheet")
    print("press 3 to view data")
    print("press 4 to exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        supplier = input("Enter supplier name: ")
        
        
        cursor.execute('''
         INSERT INTO sales (product_name, quantity, price, supplier)
        VALUES (?, ?, ?, ?)''', (product_name, quantity, price, supplier))
        
        conn.commit()
        print("Data added successfully")

    elif choice == 2:
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        
        excel_file=df.to_excel("product.xlsx", index=False, engine='openpyxl')
        print("Data exported to Excel successfully.")

    elif choice == 3:
        df= pd.read_sql_query("SELECT * FROM sales", conn)
        print(df)
        
    elif choice == 4:
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please try again.")
