import tkinter as tk
# create a main windows 
root=tk.Tk()
# create a title of your software windows
root.title("Blank windows for software or simple windows for software")
# create a windows size
root.geometry("650x550")
# create a label of windows
label=tk.Label(root,text="Hello i am a Brijesh", font=("Arial",20))
# set a position  with border and content and provides a space in content padding
label.pack(pady=50)
# print a window 
root.mainloop()
