import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# import database
from database import create_connection

# create a windows
root = ttk.Window(themename="cosmo")

# create a app title name
root.title("CRUD App Windows")

# create a geometry
root.geometry("550x500")

# create a function for user input
def input_data():
    name = entry1.get()
    age = entry2.get()
    address = entry3.get()

    print("Name:", name)
    print("Age:", age)
    print("Address:", address)


# create a label
label = ttk.Label(
    root,
    text="CRUD App Demo",
    bootstyle="primary",
    font=("Arial", 18, "bold")
)
label.pack(pady=20)


# create user label
# for Name
label1 = ttk.Label(
    root,
    text="Enter Your Name :",
    font=("Arial", 10)
)
label1.pack(pady=10)

entry1 = ttk.Entry(
    root,
    bootstyle="primary"
)
entry1.pack(pady=10)


# for age
label2 = ttk.Label(
    root,
    text="Enter Your Age :",
    font=("Arial", 10)
)
label2.pack(pady=10)

entry2 = ttk.Entry(
    root,
    bootstyle="primary"
)
entry2.pack(pady=10)


# for Address
label3 = ttk.Label(
    root,
    text="Enter Your Address :",
    font=("Arial", 10)
)
label3.pack(pady=10)

entry3 = ttk.Entry(
    root,
    bootstyle="primary"
)
entry3.pack(pady=10)


# for button
button = ttk.Button(
    root,
    text="Submit",
    command=input_data,
    bootstyle="danger"
)
button.pack(pady=15)


# create windows loop or display the windows app
root.mainloop()