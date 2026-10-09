import tkinter as tk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import tkinter.messagebox as message


# ============================================================
# MAIN WINDOW
# ============================================================

root = ttkb.Window(themename="flatly")

root.title("TOPS - Compound Interest Calculator")
root.geometry("1440x768")
root.minsize(900, 600)


# ============================================================
# FUNCTIONS
# ============================================================

def calculate_compound_interest():

    try:
        # Get values from input fields
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        # Validation
        if principal <= 0:
            message.showwarning(
                "⚠️ Invalid Amount",
                "Please enter a Principal Amount greater than 0."
            )
            return

        if rate < 0:
            message.showwarning(
                "⚠️ Invalid Rate",
                "Interest Rate cannot be negative."
            )
            return

        if time <= 0:
            message.showwarning(
                "⚠️ Invalid Time",
                "Please enter Time greater than 0."
            )
            return

        # Compound Interest Formula
        amount = principal * (1 + rate / 100) ** time

        compound_interest = amount - principal

        # Display result
        result_interest.config(
            text=f"₹ {compound_interest:,.2f}"
        )

        result_total.config(
            text=f"₹ {amount:,.2f}"
        )

        # Fancy success message
        message.showinfo(
            "🎉 Calculation Successful!",
            f"✨ Compound Interest Calculated! ✨\n\n"
            f"Principal Amount : ₹ {principal:,.2f}\n"
            f"Interest Rate    : {rate}%\n"
            f"Time             : {time} Years\n\n"
            f"📈 Compound Interest : ₹ {compound_interest:,.2f}\n"
            f"💰 Final Amount      : ₹ {amount:,.2f}\n\n"
            f"🚀 Thank you for using TOPS Calculator!"
        )

    except ValueError:

        message.showerror(
            "❌ Invalid Input",
            "Please enter valid numeric values.\n\n"
            "Example:\n"
            "Principal = 50000\n"
            "Rate = 7.5\n"
            "Time = 2"
        )


def clear_fields():

    entry_principal.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_time.delete(0, tk.END)

    result_interest.config(text="₹ 0.00")
    result_total.config(text="₹ 0.00")

    entry_principal.focus()


# ============================================================
# MAIN CONTAINER
# ============================================================

main_frame = ttkb.Frame(
    root,
    padding=30
)

main_frame.pack(
    fill=BOTH,
    expand=True
)


# ============================================================
# HEADER
# ============================================================

header_frame = ttkb.Frame(main_frame)
header_frame.pack(
    fill=X,
    pady=(0, 25)
)


title = ttkb.Label(
    header_frame,
    text="💰 TOPS Compound Interest Calculator",
    font=("Arial", 28, "bold"),
    bootstyle="primary"
)

title.pack()


subtitle = ttkb.Label(
    header_frame,
    text="Calculate your compound interest quickly, easily and accurately 🚀",
    font=("Arial", 13),
    bootstyle="secondary"
)

subtitle.pack(pady=8)


# ============================================================
# CALCULATOR CARD
# ============================================================

calculator_frame = ttkb.Frame(
    main_frame,
    padding=30,
    bootstyle="light"
)

calculator_frame.pack(
    fill=BOTH,
    expand=True
)


# Responsive columns
calculator_frame.columnconfigure(0, weight=1)
calculator_frame.columnconfigure(1, weight=2)
calculator_frame.columnconfigure(2, weight=1)

calculator_frame.rowconfigure(0, weight=1)


# ============================================================
# LEFT INFORMATION PANEL
# ============================================================

info_frame = ttkb.Frame(
    calculator_frame,
    padding=25
)

info_frame.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=15
)


info_title = ttkb.Label(
    info_frame,
    text="📊 Compound Interest",
    font=("Arial", 20, "bold"),
    bootstyle="primary"
)

info_title.pack(
    pady=(20, 15)
)


info_text = ttkb.Label(
    info_frame,
    text=(
        "Compound Interest is calculated\n"
        "using the following formula:\n\n"
        "A = P × (1 + R / 100)ᵀ\n\n"
        "CI = A - P\n\n"
        "P = Principal Amount\n"
        "R = Rate of Interest\n"
        "T = Time in Years\n"
        "A = Final Amount"
    ),
    font=("Arial", 13),
    justify="center"
)

info_text.pack(
    pady=20
)


# ============================================================
# INPUT FORM
# ============================================================

form_frame = ttkb.Frame(
    calculator_frame,
    padding=25
)

form_frame.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=15
)


form_title = ttkb.Label(
    form_frame,
    text="📝 Enter Your Details",
    font=("Arial", 20, "bold"),
    bootstyle="success"
)

form_title.pack(
    pady=(10, 25)
)


# ============================================================
# PRINCIPAL AMOUNT
# ============================================================

label_principal = ttkb.Label(
    form_frame,
    text="💵 Principal Amount (₹)",
    font=("Arial", 12, "bold")
)

label_principal.pack(
    anchor="w",
    pady=(5, 5)
)


entry_principal = ttkb.Entry(
    form_frame,
    font=("Arial", 14)
)

entry_principal.pack(
    fill=X,
    ipady=8,
    pady=(0, 15)
)


# ============================================================
# INTEREST RATE
# ============================================================

label_rate = ttkb.Label(
    form_frame,
    text="📈 Annual Interest Rate (%)",
    font=("Arial", 12, "bold")
)

label_rate.pack(
    anchor="w",
    pady=(5, 5)
)


entry_rate = ttkb.Entry(
    form_frame,
    font=("Arial", 14)
)

entry_rate.pack(
    fill=X,
    ipady=8,
    pady=(0, 15)
)


# ============================================================
# TIME
# ============================================================

label_time = ttkb.Label(
    form_frame,
    text="⏰ Time (Years)",
    font=("Arial", 12, "bold")
)

label_time.pack(
    anchor="w",
    pady=(5, 5)
)


entry_time = ttkb.Entry(
    form_frame,
    font=("Arial", 14)
)

entry_time.pack(
    fill=X,
    ipady=8,
    pady=(0, 20)
)


# ============================================================
# BUTTONS
# ============================================================

button_frame = ttkb.Frame(form_frame)
button_frame.pack(
    fill=X,
    pady=10
)


calculate_button = ttkb.Button(
    button_frame,
    text="🧮 Calculate Compound Interest",
    command=calculate_compound_interest,
    bootstyle="success",
    padding=12
)

calculate_button.pack(
    side=LEFT,
    expand=True,
    fill=X,
    padx=(0, 5)
)


clear_button = ttkb.Button(
    button_frame,
    text="🔄 Clear",
    command=clear_fields,
    bootstyle="secondary",
    padding=12
)

clear_button.pack(
    side=LEFT,
    expand=True,
    fill=X,
    padx=(5, 0)
)


# ============================================================
# RIGHT RESULT PANEL
# ============================================================

result_frame = ttkb.Frame(
    calculator_frame,
    padding=25
)

result_frame.grid(
    row=0,
    column=2,
    sticky="nsew",
    padx=15
)


result_title = ttkb.Label(
    result_frame,
    text="🎯 Your Result",
    font=("Arial", 20, "bold"),
    bootstyle="warning"
)

result_title.pack(
    pady=(20, 30)
)


# ============================================================
# COMPOUND INTEREST RESULT
# ============================================================

interest_label = ttkb.Label(
    result_frame,
    text="Compound Interest",
    font=("Arial", 12, "bold")
)

interest_label.pack(
    pady=(10, 5)
)


result_interest = ttkb.Label(
    result_frame,
    text="₹ 0.00",
    font=("Arial", 24, "bold"),
    bootstyle="success"
)

result_interest.pack(
    pady=(0, 30)
)


# ============================================================
# FINAL AMOUNT
# ============================================================

total_label = ttkb.Label(
    result_frame,
    text="Final Amount",
    font=("Arial", 12, "bold")
)

total_label.pack(
    pady=(10, 5)
)


result_total = ttkb.Label(
    result_frame,
    text="₹ 0.00",
    font=("Arial", 24, "bold"),
    bootstyle="primary"
)

result_total.pack(
    pady=(0, 30)
)


# ============================================================
# FOOTER
# ============================================================

footer = ttkb.Label(
    main_frame,
    text="✨ TOPS Technologies | Compound Interest Calculator ✨",
    font=("Arial", 11),
    bootstyle="secondary"
)

footer.pack(
    pady=(15, 0)
)


# ============================================================
# DEFAULT FOCUS
# ============================================================

entry_principal.focus()


# ============================================================
# RUN APPLICATION
# ============================================================

root.mainloop()