import tkinter as tk
# pass a message 
import tkinter.messagebox as messagebox
# create a main windows 
root=tk.Tk()
# create a title of your software windows
root.title("Take input from users create windows")
# create a windows size
root.geometry("650x550")
# create a function for print input values 
def input_user():
    user_input=entry.get()
    # print a message
    return messagebox.showinfo("user Input data is :",f"Hello ,{user_input}")
# create a label of windows
label=tk.Label(root,text="Enter Your Name : ", fg="coral", font=("Arial",18))
# set a position  with border and content and provides a space in content padding
label.pack(pady=15)
#create input 
entry=tk.Entry(root,text="Enter your Name :", font=("Arial",18))
entry.pack(pady=15)

# create a button widget
button=tk.Button(root,text="Submit",command=input_user)
button.pack(pady=15)

# print a window 
root.mainloop()
