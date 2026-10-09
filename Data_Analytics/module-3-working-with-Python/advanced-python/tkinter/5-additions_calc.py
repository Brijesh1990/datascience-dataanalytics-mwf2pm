import tkinter as tk
# pass a message 
import tkinter.messagebox as messagebox
# create a main windows 
root=tk.Tk()
# create a title of your software windows
root.title("Take input from users create windows")
# create a windows size
root.geometry("650x550")
# create a function for additions of numbers 
def addinfo():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a+b
    # print a message
    return messagebox.showinfo("Additions of Numbers is  :",f"Additions of Numbers is : ,{c}")
# create a label of windows
label1=tk.Label(root,text="Enter a values : ", fg="coral", font=("Arial",18))
# set a position  with border and content and provides a space in content padding
label1.pack(pady=15)
#create input 
entry1=tk.Entry(root,text="Enter a values :", font=("Arial",18))
entry1.pack(pady=15)

# create a label of windows
label2=tk.Label(root,text="Enter b values : ", fg="coral", font=("Arial",18))
# set a position  with border and content and provides a space in content padding
label2.pack(pady=15)
#create input 
entry2=tk.Entry(root,text="Enter b values :", font=("Arial",18))
entry2.pack(pady=15)

# create a button widget
button=tk.Button(root,text="Click To Add",command= addinfo)
button.pack(pady=15)

# print a window 
root.mainloop()
