import tkinter as tk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import tkinter.messagebox as message


# ============================================================
# MAIN WINDOW
# ============================================================

root = ttkb.Window(themename="flatly")

root.title("TOPS - Login App")
root.geometry("1440x768")
root.minsize(900, 600)


# ============================================================
# COLORS
# ============================================================

PRIMARY = "#0d6efd"
DARK = "#172033"
LIGHT = "#f5f7fb"
WHITE = "#ffffff"
TEXT = "#333333"
MUTED = "#777777"


# ============================================================
# RESPONSIVE MAIN CONTAINER
# ============================================================

main_frame = tk.Frame(root, bg=LIGHT)
main_frame.pack(fill="both", expand=True)

# Two columns
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)


# ============================================================
# LEFT PANEL
# ============================================================

left_panel = tk.Frame(
    main_frame,
    bg=PRIMARY
)

left_panel.grid(
    row=0,
    column=0,
    sticky="nsew"
)

left_panel.columnconfigure(0, weight=1)
left_panel.rowconfigure(0, weight=1)


# Content inside left panel
left_content = tk.Frame(
    left_panel,
    bg=PRIMARY
)

left_content.grid(
    row=0,
    column=0
)


# TOPS Logo / Brand
logo = tk.Label(
    left_content,
    text="TOPS",
    font=("Arial", 48, "bold"),
    bg=PRIMARY,
    fg=WHITE
)

logo.pack(pady=(20, 10))


subtitle = tk.Label(
    left_content,
    text="TECHNOLOGY",
    font=("Arial", 14, "bold"),
    bg=PRIMARY,
    fg=WHITE
)

subtitle.pack()


# Welcome text
welcome = tk.Label(
    left_content,
    text="Welcome to TOPS",
    font=("Arial", 30, "bold"),
    bg=PRIMARY,
    fg=WHITE
)

welcome.pack(pady=(60, 10))


description = tk.Label(
    left_content,
    text=(
        "Learn. Build. Grow.\n\n"
        "Your learning and technology journey\n"
        "starts here."
    ),
    font=("Arial", 15),
    bg=PRIMARY,
    fg=WHITE,
    justify="center"
)

description.pack()


# Decorative text
features = tk.Label(
    left_content,
    text="✓ Training     ✓ Development     ✓ Career",
    font=("Arial", 12),
    bg=PRIMARY,
    fg=WHITE
)

features.pack(pady=40)


# ============================================================
# RIGHT PANEL
# ============================================================

right_panel = tk.Frame(
    main_frame,
    bg=WHITE
)

right_panel.grid(
    row=0,
    column=1,
    sticky="nsew"
)

right_panel.columnconfigure(0, weight=1)
right_panel.rowconfigure(0, weight=1)


# Login card
login_card = tk.Frame(
    right_panel,
    bg=WHITE
)

login_card.grid(
    row=0,
    column=0
)


# ============================================================
# LOGIN HEADER
# ============================================================

login_title = tk.Label(
    login_card,
    text="Welcome Back!",
    font=("Arial", 30, "bold"),
    bg=WHITE,
    fg=DARK
)

login_title.pack(
    pady=(10, 5)
)


login_subtitle = tk.Label(
    login_card,
    text="Login to continue to your account",
    font=("Arial", 12),
    bg=WHITE,
    fg=MUTED
)

login_subtitle.pack(
    pady=(0, 30)
)


# ============================================================
# EMAIL
# ============================================================

email_label = tk.Label(
    login_card,
    text="Email Address",
    font=("Arial", 11, "bold"),
    bg=WHITE,
    fg=TEXT,
    anchor="w"
)

email_label.pack(
    fill="x",
    pady=(5, 5)
)


email_entry = ttkb.Entry(
    login_card,
    width=40,
    font=("Arial", 12)
)

email_entry.pack(
    ipady=8,
    fill="x"
)


# ============================================================
# PASSWORD
# ============================================================

password_label = tk.Label(
    login_card,
    text="Password",
    font=("Arial", 11, "bold"),
    bg=WHITE,
    fg=TEXT,
    anchor="w"
)

password_label.pack(
    fill="x",
    pady=(20, 5)
)


password_frame = tk.Frame(
    login_card,
    bg=WHITE
)

password_frame.pack(
    fill="x"
)


password_entry = ttkb.Entry(
    password_frame,
    font=("Arial", 12),
    show="*"
)

password_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=8
)


# ============================================================
# SHOW / HIDE PASSWORD
# ============================================================

show_password = tk.BooleanVar(value=False)


def toggle_password():

    if show_password.get():
        password_entry.config(show="")
        show_btn.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_btn.config(text="Show")


show_btn = ttkb.Button(
    password_frame,
    text="Show",
    bootstyle="secondary-outline",
    command=toggle_password
)

show_btn.pack(
    side="right",
    padx=(8, 0),
    ipady=5
)


# ============================================================
# REMEMBER ME + FORGOT PASSWORD
# ============================================================

options_frame = tk.Frame(
    login_card,
    bg=WHITE
)

options_frame.pack(
    fill="x",
    pady=20
)


remember_var = tk.BooleanVar()


remember_check = ttkb.Checkbutton(
    options_frame,
    text="Remember me",
    variable=remember_var,
    bootstyle="primary"
)

remember_check.pack(
    side="left"
)


def forgot_password():

    message.showinfo(
        "Forgot Password",
        "Password reset link functionality will be added here."
    )


forgot_btn = tk.Label(
    options_frame,
    text="Forgot Password?",
    font=("Arial", 10, "underline"),
    bg=WHITE,
    fg=PRIMARY,
    cursor="hand2"
)

forgot_btn.pack(
    side="right"
)

forgot_btn.bind(
    "<Button-1>",
    lambda event: forgot_password()
)


# ============================================================
# LOGIN FUNCTION
# ============================================================

def login():

    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if email == "":
        message.showwarning(
            "Validation",
            "Please enter your email address."
        )
        email_entry.focus()
        return

    if password == "":
        message.showwarning(
            "Validation",
            "Please enter your password."
        )
        password_entry.focus()
        return

    # Sample login
    if email == "admin@tops.com" and password == "123456":

        message.showinfo(
            "Login Successful",
            "Welcome to TOPS Technology!"
        )

        show_dashboard()

    else:

        message.showerror(
            "Login Failed",
            "Invalid email or password."
        )


# ============================================================
# LOGIN BUTTON
# ============================================================

login_btn = ttkb.Button(
    login_card,
    text="LOGIN",
    bootstyle="primary",
    command=login
)

login_btn.pack(
    fill="x",
    ipady=8,
    pady=(5, 20)
)


# ============================================================
# REGISTER
# ============================================================

register_frame = tk.Frame(
    login_card,
    bg=WHITE
)

register_frame.pack(
    pady=10
)


register_text = tk.Label(
    register_frame,
    text="Don't have an account?",
    font=("Arial", 10),
    bg=WHITE,
    fg=MUTED
)

register_text.pack(
    side="left"
)


register_btn = tk.Label(
    register_frame,
    text=" Register Now",
    font=("Arial", 10, "bold"),
    bg=WHITE,
    fg=PRIMARY,
    cursor="hand2"
)

register_btn.pack(
    side="left"
)


# ============================================================
# DASHBOARD
# ============================================================

def show_dashboard():

    # Remove login screen
    for widget in main_frame.winfo_children():
        widget.destroy()

    main_frame.configure(bg=LIGHT)

    # Header
    header = tk.Frame(
        main_frame,
        bg=PRIMARY,
        height=75
    )

    header.pack(
        fill="x"
    )

    header.pack_propagate(False)

    title = tk.Label(
        header,
        text="TOPS TECHNOLOGY",
        font=("Arial", 22, "bold"),
        bg=PRIMARY,
        fg=WHITE
    )

    title.pack(
        side="left",
        padx=30
    )


    def logout():

        answer = message.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if answer:
            root.destroy()


    logout_btn = ttkb.Button(
        header,
        text="Logout",
        bootstyle="light-outline",
        command=logout
    )

    logout_btn.pack(
        side="right",
        padx=30
    )


    # Dashboard content
    dashboard = tk.Frame(
        main_frame,
        bg=LIGHT
    )

    dashboard.pack(
        fill="both",
        expand=True,
        padx=40,
        pady=40
    )


    dashboard.columnconfigure(
        (0, 1, 2),
        weight=1
    )


    welcome_dashboard = tk.Label(
        dashboard,
        text="Dashboard",
        font=("Arial", 30, "bold"),
        bg=LIGHT,
        fg=DARK
    )

    welcome_dashboard.grid(
        row=0,
        column=0,
        columnspan=3,
        sticky="w",
        pady=(0, 30)
    )


    # Cards
    create_card(
        dashboard,
        1,
        0,
        "Students",
        "1,250"
    )

    create_card(
        dashboard,
        1,
        1,
        "Courses",
        "25"
    )

    create_card(
        dashboard,
        1,
        2,
        "Trainers",
        "48"
    )


# ============================================================
# DASHBOARD CARD
# ============================================================

def create_card(parent, row, column, title, value):

    card = tk.Frame(
        parent,
        bg=WHITE,
        bd=1,
        relief="solid"
    )

    card.grid(
        row=row,
        column=column,
        sticky="nsew",
        padx=10,
        pady=10,
        ipadx=20,
        ipady=25
    )


    title_label = tk.Label(
        card,
        text=title,
        font=("Arial", 13),
        bg=WHITE,
        fg=MUTED
    )

    title_label.pack(
        pady=(10, 5)
    )


    value_label = tk.Label(
        card,
        text=value,
        font=("Arial", 28, "bold"),
        bg=WHITE,
        fg=PRIMARY
    )

    value_label.pack(
        pady=(5, 10)
    )


# ============================================================
# ENTER KEY LOGIN
# ============================================================

root.bind(
    "<Return>",
    lambda event: login()
)


# ============================================================
# START APPLICATION
# ============================================================

email_entry.focus()

root.mainloop()