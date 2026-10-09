import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# import database
from database import create_connection

# create a windows
root = ttk.Window(themename="cosmo")

# create a app title name
root.title("Task Manager App")

# create a geometry
root.geometry("1100x700")

# create a function for user input
def input_data():
    tasktitle = entry1.get()
    added_date = entry2.get()
    assign_to = entry3.get()
    status = status_combo.get()

    print("Task Title:", tasktitle)
    print("Added Date:", added_date)
    print("Assign To:", assign_to)
    print("Status:", status)


# ==========================================================
# ANIMATED HEADER IMAGE / ICON
# ==========================================================

animation_frames = [
    "📋",
    "📝",
    "⏰",
    "✅",
    "🌟"
]

animation_index = 0


def animate_image():
    global animation_index

    animation_label.config(
        text=animation_frames[animation_index]
    )

    animation_index += 1

    if animation_index >= len(animation_frames):
        animation_index = 0

    root.after(600, animate_image)


# ==========================================================
# MAIN BACKGROUND
# ==========================================================

main_frame = ttk.Frame(
    root,
    padding=20,
    bootstyle="light"
)

main_frame.pack(
    fill=BOTH,
    expand=True
)


# ==========================================================
# HEADER
# ==========================================================

header_frame = ttk.Frame(
    main_frame,
    padding=20,
    bootstyle="primary"
)

header_frame.pack(
    fill=X,
    pady=(0, 15)
)


title_frame = ttk.Frame(
    header_frame,
    bootstyle="primary"
)

title_frame.pack(
    side=LEFT,
    fill=X,
    expand=True
)


# create a label
label = ttk.Label(
    title_frame,
    text="TASK MANAGER",
    bootstyle="inverse-primary",
    font=("Arial", 25, "bold")
)

label.pack(
    anchor=W
)


ttk.Label(
    title_frame,
    text="Plan • Organize • Achieve",
    bootstyle="inverse-primary",
    font=("Arial", 11)
).pack(
    anchor=W,
    pady=(5, 0)
)


# Animated image
animation_label = ttk.Label(
    header_frame,
    text="📋",
    bootstyle="inverse-primary",
    font=("Segoe UI Emoji", 45)
)

animation_label.pack(
    side=RIGHT,
    padx=20
)

animate_image()


# ==========================================================
# WELCOME BANNER
# ==========================================================

welcome_frame = ttk.Frame(
    main_frame,
    padding=15,
    bootstyle="info"
)

welcome_frame.pack(
    fill=X,
    pady=(0, 15)
)


ttk.Label(
    welcome_frame,
    text="👋 Welcome to your Task Manager",
    bootstyle="inverse-info",
    font=("Arial", 17, "bold")
).pack(
    anchor=W
)


ttk.Label(
    welcome_frame,
    text="Stay focused, manage your tasks and get things done!",
    bootstyle="inverse-info",
    font=("Arial", 10)
).pack(
    anchor=W,
    pady=(5, 0)
)


# ==========================================================
# ADD TASK CARD
# ==========================================================

form_frame = ttk.Labelframe(
    main_frame,
    text="  ➕ ADD NEW TASK  ",
    padding=20,
    bootstyle="primary"
)

form_frame.pack(
    fill=X,
    pady=(0, 15)
)


# ----------------------------------------------------------
# Task Title
# ----------------------------------------------------------

label1 = ttk.Label(
    form_frame,
    text="Task Title",
    font=("Arial", 10, "bold")
)

label1.grid(
    row=0,
    column=0,
    sticky=W,
    padx=10,
    pady=(5, 5)
)


entry1 = ttk.Entry(
    form_frame,
    bootstyle="primary",
    width=28
)

entry1.grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


# ----------------------------------------------------------
# Added Date
# ----------------------------------------------------------

label2 = ttk.Label(
    form_frame,
    text="Added Date",
    font=("Arial", 10, "bold")
)

label2.grid(
    row=0,
    column=1,
    sticky=W,
    padx=10,
    pady=(5, 5)
)


entry2 = ttk.Entry(
    form_frame,
    bootstyle="info",
    width=22
)

entry2.insert(
    0,
    "2026-09-18"
)

entry2.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


# ----------------------------------------------------------
# Assign To
# ----------------------------------------------------------

label3 = ttk.Label(
    form_frame,
    text="Assign To",
    font=("Arial", 10, "bold")
)

label3.grid(
    row=0,
    column=2,
    sticky=W,
    padx=10,
    pady=(5, 5)
)


entry3 = ttk.Entry(
    form_frame,
    bootstyle="success",
    width=22
)

entry3.grid(
    row=1,
    column=2,
    padx=10,
    pady=5
)


# ----------------------------------------------------------
# Status
# ----------------------------------------------------------

label4 = ttk.Label(
    form_frame,
    text="Status",
    font=("Arial", 10, "bold")
)

label4.grid(
    row=0,
    column=3,
    sticky=W,
    padx=10,
    pady=(5, 5)
)


status_combo = ttk.Combobox(
    form_frame,
    values=[
        "Pending",
        "In Progress",
        "Completed"
    ],
    state="readonly",
    width=18,
    bootstyle="warning"
)

status_combo.set("Pending")

status_combo.grid(
    row=1,
    column=3,
    padx=10,
    pady=5
)


# ----------------------------------------------------------
# Add Task Button
# ----------------------------------------------------------

button = ttk.Button(
    form_frame,
    text="➕  Add Task",
    command=input_data,
    bootstyle="success",
    width=16
)

button.grid(
    row=1,
    column=4,
    padx=15,
    pady=5
)


# ==========================================================
# TASK LIST HEADER
# ==========================================================

task_header = ttk.Frame(
    main_frame
)

task_header.pack(
    fill=X,
    pady=(5, 8)
)


ttk.Label(
    task_header,
    text="📋  My Tasks",
    font=("Arial", 18, "bold"),
    bootstyle="primary"
).pack(
    side=LEFT
)


ttk.Label(
    task_header,
    text="Manage your daily activities",
    font=("Arial", 10),
    bootstyle="secondary"
).pack(
    side=RIGHT
)


# ==========================================================
# TASK TABLE
# ==========================================================

table_frame = ttk.Frame(
    main_frame,
    padding=10,
    bootstyle="light"
)

table_frame.pack(
    fill=BOTH,
    expand=True
)


columns = (
    "ID",
    "Task Title",
    "Added Date",
    "Assign To",
    "Status"
)


task_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=9,
    bootstyle="primary"
)


task_table.heading(
    "ID",
    text="#"
)

task_table.heading(
    "Task Title",
    text="Task Title"
)

task_table.heading(
    "Added Date",
    text="Added Date"
)

task_table.heading(
    "Assign To",
    text="Assign To"
)

task_table.heading(
    "Status",
    text="Status"
)


task_table.column(
    "ID",
    width=60,
    anchor=CENTER
)

task_table.column(
    "Task Title",
    width=300,
    anchor=W
)

task_table.column(
    "Added Date",
    width=160,
    anchor=CENTER
)

task_table.column(
    "Assign To",
    width=200,
    anchor=W
)

task_table.column(
    "Status",
    width=180,
    anchor=CENTER
)


# Sample design data
task_table.insert(
    "",
    END,
    values=(
        "1",
        "Complete Python Project",
        "2026-09-18",
        "Brijesh Pandey",
        "Pending"
    )
)

task_table.insert(
    "",
    END,
    values=(
        "2",
        "Prepare Presentation",
        "2026-09-17",
        "Vanshika",
        "In Progress"
    )
)

task_table.insert(
    "",
    END,
    values=(
        "3",
        "Database Design",
        "2026-09-16",
        "Amit Gupta",
        "Completed"
    )
)

task_table.insert(
    "",
    END,
    values=(
        "4",
        "UI/UX Design",
        "2026-09-15",
        "Neha Sharma",
        "In Progress"
    )
)


task_table.pack(
    fill=BOTH,
    expand=True
)


# ==========================================================
# BOTTOM BUTTONS
# ==========================================================

bottom_frame = ttk.Frame(
    main_frame
)

bottom_frame.pack(
    fill=X,
    pady=(10, 0)
)


ttk.Button(
    bottom_frame,
    text="✏️ Edit Task",
    bootstyle="warning",
    width=15
).pack(
    side=LEFT,
    padx=5
)


ttk.Button(
    bottom_frame,
    text="🗑️ Delete Task",
    bootstyle="danger",
    width=15
).pack(
    side=LEFT,
    padx=5
)


ttk.Button(
    bottom_frame,
    text="🔄 Refresh",
    bootstyle="info",
    width=15
).pack(
    side=LEFT,
    padx=5
)


# ==========================================================
# STATISTICS CARDS
# ==========================================================

stats_frame = ttk.Frame(
    main_frame
)

stats_frame.pack(
    fill=X,
    pady=(15, 0)
)


def create_stat_card(
    parent,
    icon,
    number,
    title,
    style
):

    card = ttk.Frame(
        parent,
        padding=10,
        bootstyle=style
    )

    card.pack(
        side=LEFT,
        fill=X,
        expand=True,
        padx=5
    )

    ttk.Label(
        card,
        text=icon,
        font=("Segoe UI Emoji", 22),
        bootstyle=f"inverse-{style}"
    ).pack(
        side=LEFT,
        padx=8
    )

    info = ttk.Frame(
        card,
        bootstyle=style
    )

    info.pack(
        side=LEFT
    )

    ttk.Label(
        info,
        text=number,
        font=("Arial", 18, "bold"),
        bootstyle=f"inverse-{style}"
    ).pack(
        anchor=W
    )

    ttk.Label(
        info,
        text=title,
        font=("Arial", 9),
        bootstyle=f"inverse-{style}"
    ).pack(
        anchor=W
    )


create_stat_card(
    stats_frame,
    "📋",
    "4",
    "Total Tasks",
    "primary"
)


create_stat_card(
    stats_frame,
    "⏰",
    "1",
    "Pending",
    "warning"
)


create_stat_card(
    stats_frame,
    "⚙️",
    "2",
    "In Progress",
    "info"
)


create_stat_card(
    stats_frame,
    "✅",
    "1",
    "Completed",
    "success"
)


# ==========================================================
# FOOTER
# ==========================================================

ttk.Label(
    main_frame,
    text="🚀 Stay productive • Plan better • Achieve more",
    font=("Arial", 9, "italic"),
    bootstyle="secondary"
).pack(
    pady=(10, 0)
)


# create windows loop or display the windows app
root.mainloop()