import tkinter as tk
from tkinter import filedialog, messagebox


# =========================================================
# Main Window
# =========================================================

root = tk.Tk()

root.title("Untitled - Notepad")
root.geometry("750x550")


# Store current file
current_file = None


# =========================================================
# Functions
# =========================================================

def new_file():
    global current_file

    text_area.delete("1.0", tk.END)

    current_file = None

    root.title("Untitled - Notepad")


def open_file():
    global current_file

    file = filedialog.askopenfilename(
        title="Open File",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if file:

        with open(file, "r", encoding="utf-8") as f:
            data = f.read()

        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", data)

        current_file = file

        root.title(file + " - Notepad")


def save_file():

    global current_file

    # If file does not exist, use Save As
    if current_file is None:
        save_as()
        return

    data = text_area.get("1.0", tk.END)

    with open(current_file, "w", encoding="utf-8") as f:
        f.write(data)

    root.title(current_file + " - Notepad")

    messagebox.showinfo(
        "Notepad",
        "File saved successfully!"
    )


def save_as():

    global current_file

    file = filedialog.asksaveasfilename(
        title="Save As",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if file:

        data = text_area.get("1.0", tk.END)

        with open(file, "w", encoding="utf-8") as f:
            f.write(data)

        current_file = file

        root.title(file + " - Notepad")


def exit_app():

    answer = messagebox.askyesno(
        "Exit",
        "Do you want to exit Notepad?"
    )

    if answer:
        root.destroy()


def cut_text():
    text_area.event_generate("<<Cut>>")


def copy_text():
    text_area.event_generate("<<Copy>>")


def paste_text():
    text_area.event_generate("<<Paste>>")


def select_all():
    text_area.tag_add(
        "sel",
        "1.0",
        "end"
    )


def undo_text():
    try:
        text_area.edit_undo()
    except:
        pass


def redo_text():
    try:
        text_area.edit_redo()
    except:
        pass


def find_text():

    find_window = tk.Toplevel(root)

    find_window.title("Find")

    find_window.geometry("350x100")

    tk.Label(
        find_window,
        text="Find:"
    ).pack(side=tk.LEFT, padx=10)

    search_box = tk.Entry(
        find_window,
        width=25
    )

    search_box.pack(
        side=tk.LEFT,
        padx=5
    )

    search_box.focus()

    def search():

        text_area.tag_remove(
            "found",
            "1.0",
            tk.END
        )

        word = search_box.get()

        if word:

            start = "1.0"

            while True:

                start = text_area.search(
                    word,
                    start,
                    stopindex=tk.END
                )

                if not start:
                    break

                end = f"{start}+{len(word)}c"

                text_area.tag_add(
                    "found",
                    start,
                    end
                )

                start = end

            text_area.tag_config(
                "found",
                background="yellow",
                foreground="black"
            )

    tk.Button(
        find_window,
        text="Find",
        command=search
    ).pack(side=tk.LEFT)


def word_wrap():

    if wrap_var.get():

        text_area.config(
            wrap=tk.WORD
        )

    else:

        text_area.config(
            wrap=tk.NONE
        )


def about_notepad():

    messagebox.showinfo(
        "About Notepad",
        "Simple Notepad Application\n\n"
        "Created using Python Tkinter\n"
        "Developer: Brijesh"
    )


# =========================================================
# Menu Bar
# =========================================================

menu_bar = tk.Menu(root)


# =========================================================
# File Menu
# =========================================================

file_menu = tk.Menu(
    menu_bar,
    tearoff=0
)

file_menu.add_command(
    label="New",
    accelerator="Ctrl+N",
    command=new_file
)

file_menu.add_command(
    label="Open...",
    accelerator="Ctrl+O",
    command=open_file
)

file_menu.add_command(
    label="Save",
    accelerator="Ctrl+S",
    command=save_file
)

file_menu.add_command(
    label="Save As...",
    accelerator="Ctrl+Shift+S",
    command=save_as
)

file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=exit_app
)

menu_bar.add_cascade(
    label="File",
    menu=file_menu
)


# =========================================================
# Edit Menu
# =========================================================

edit_menu = tk.Menu(
    menu_bar,
    tearoff=0
)

edit_menu.add_command(
    label="Undo",
    accelerator="Ctrl+Z",
    command=undo_text
)

edit_menu.add_command(
    label="Redo",
    accelerator="Ctrl+Y",
    command=redo_text
)

edit_menu.add_separator()

edit_menu.add_command(
    label="Cut",
    accelerator="Ctrl+X",
    command=cut_text
)

edit_menu.add_command(
    label="Copy",
    accelerator="Ctrl+C",
    command=copy_text
)

edit_menu.add_command(
    label="Paste",
    accelerator="Ctrl+V",
    command=paste_text
)

edit_menu.add_command(
    label="Select All",
    accelerator="Ctrl+A",
    command=select_all
)

edit_menu.add_separator()

edit_menu.add_command(
    label="Find",
    accelerator="Ctrl+F",
    command=find_text
)

menu_bar.add_cascade(
    label="Edit",
    menu=edit_menu
)


# =========================================================
# Format Menu
# =========================================================

format_menu = tk.Menu(
    menu_bar,
    tearoff=0
)

wrap_var = tk.BooleanVar(value=True)

format_menu.add_checkbutton(
    label="Word Wrap",
    variable=wrap_var,
    command=word_wrap
)

menu_bar.add_cascade(
    label="Format",
    menu=format_menu
)


# =========================================================
# View Menu
# =========================================================

view_menu = tk.Menu(
    menu_bar,
    tearoff=0
)

view_menu.add_command(
    label="Status Bar",
    command=lambda: messagebox.showinfo(
        "Status Bar",
        "Status Bar is enabled."
    )
)

menu_bar.add_cascade(
    label="View",
    menu=view_menu
)


# =========================================================
# Help Menu
# =========================================================

help_menu = tk.Menu(
    menu_bar,
    tearoff=0
)

help_menu.add_command(
    label="About Notepad",
    command=about_notepad
)

menu_bar.add_cascade(
    label="Help",
    menu=help_menu
)


# Add Menu Bar to Window

root.config(
    menu=menu_bar
)


# =========================================================
# Text Area + Scrollbar
# =========================================================

main_frame = tk.Frame(root)

main_frame.pack(
    fill=tk.BOTH,
    expand=True
)


# Scrollbar

scrollbar = tk.Scrollbar(
    main_frame
)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)


# Text Area

text_area = tk.Text(
    main_frame,
    font=("Consolas", 12),
    undo=True,
    wrap=tk.WORD,
    padx=5,
    pady=5,
    yscrollcommand=scrollbar.set
)

text_area.pack(
    side=tk.LEFT,
    fill=tk.BOTH,
    expand=True
)


# Connect scrollbar

scrollbar.config(
    command=text_area.yview
)


# =========================================================
# Keyboard Shortcuts
# =========================================================

root.bind(
    "<Control-n>",
    lambda event: new_file()
)

root.bind(
    "<Control-o>",
    lambda event: open_file()
)

root.bind(
    "<Control-s>",
    lambda event: save_file()
)

root.bind(
    "<Control-S>",
    lambda event: save_as()
)

root.bind(
    "<Control-f>",
    lambda event: find_text()
)

root.bind(
    "<Control-z>",
    lambda event: undo_text()
)

root.bind(
    "<Control-y>",
    lambda event: redo_text()
)


# =========================================================
# Start Application
# =========================================================

root.mainloop()