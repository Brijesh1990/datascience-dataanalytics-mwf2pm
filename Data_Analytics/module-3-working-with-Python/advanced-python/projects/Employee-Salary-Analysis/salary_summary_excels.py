import pandas as pd
import matplotlib.pyplot as plt

data={
    "employee_name":["meet","aksh","faiz","forum","pranav","mishri","rupa","astha","krunal","rupesh"],
    "departments":["IT","CSE","IT","HR","EC","EE","CSE","IT","HR","CSE"],
    "salaries":[18500,19500,20500,21500,22500,23500,24500,26500,28500,32800]
}


# create a tabular layout 
df=pd.DataFrame(data)
print(df)
# subtotal of salaries 
print("------------------------------------------")
# subtotals of salries
print("subtotals of salaries is :",df["salaries"].sum())
total_salary=df["salaries"].sum()
print("------------------------------------------")
# average   salries of employee
print("Average  salaries of employee :",df["salaries"].mean())
average_salary=df["salaries"].mean()
# get employees details who get more than average salary
print("------------------------------------------\n")
print("Employee details who get > salary than average salary :",df[df["salaries"] > average_salary])

# average greater than employees salary
employee_average_salary=df[df["salaries"] > average_salary]
print(employee_average_salary)

# ==========================================
# LINE CHART - ALL EMPLOYEES
# ==========================================

plt.figure(figsize=(8, 4))

plt.plot(
    employee_average_salary["employee_name"],
    employee_average_salary["salaries"],
    marker="o",
    linewidth=2
)

# Display salary value on each point
for i, salary in enumerate(df["salaries"]):
    plt.text(
        i,
        salary + 500,
        str(salary),
        ha="center"
    )

plt.title("Employee Salary Line Chart")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
# generate salary summary  in excel 

summary = pd.DataFrame({
    "Salary Summary": [
        "Total Salary",
        "Average Salary"
    ],
    "Amount": [
        total_salary,
        average_salary
    ]
})

# Write both DataFrames to Excel
with pd.ExcelWriter("employee_summary_salary.xlsx", engine="openpyxl") as writer:

    # Employee data
    df.to_excel(
        writer,
        sheet_name="Employees",
        index=False
    )

    # Salary summary
    summary.to_excel(
        writer,
        sheet_name="Salary Summary",
        index=False
    )
print("Excel file generated successfully: employee_summary_salary.xlsx")
plt.show()
