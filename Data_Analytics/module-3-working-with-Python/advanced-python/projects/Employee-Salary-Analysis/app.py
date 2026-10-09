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
print("------------------------------------------")
# average   salries of employee
print("Average  salaries of employee :",df["salaries"].mean())
average_salary=df["salaries"].mean()
# get employees details who get more than average salary
print("------------------------------------------\n")
print("Employee details who get > salary than average salary :",df[df["salaries"] > average_salary])

# avrege greater than employees salary
employee_average_salary=df[df["salaries"] > average_salary]
print(employee_average_salary)


# views average_salary data of employee in chart

# plt.figure(figsize=(10, 6))

# plt.bar(
#     employee_average_salary["employee_name"],
#     employee_average_salary["salaries"]
# )

# plt.title("Employees Earning More Than Average Salary")
# plt.xlabel("Employee Name")
# plt.ylabel("Salary")

# # Show salary values above bars
# for i, salary in enumerate(employee_average_salary["salaries"]):
#     plt.text(
#         i,
#         salary + 300,
#         str(salary),
#         ha="center"
#     )

# plt.xticks(rotation=45)
# plt.tight_layout()


# create a pie chart for this

# -------------------------------
# PIE CHART
# -------------------------------

# plt.figure(figsize=(8, 8))

# plt.pie(
#     employee_average_salary["salaries"],
#     labels=employee_average_salary["employee_name"],
#     autopct="%1.1f%%",
#     startangle=90
# )

# plt.title("Employees Earning More Than Average Salary")


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


# generate data in excel 
generate_date_excel=df.to_excel('employee.xlsx', engine="openpyxl",index=False)
print("Excel files generated successfully",generate_date_excel);

# # generated data in csv
# generate_date_excel=df.to_csv('employee1.xlsx', index=False)
# print("Excel files generated successfully",generate_date_excel);


# generated data in json

# generate_date_excel=df.to_json('employee2.json', index=False)
# print("Excel files generated successfully",generate_date_excel);

# display chart
plt.show()


