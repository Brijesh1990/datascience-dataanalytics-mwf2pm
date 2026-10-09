import pandas as pd
df=pd.read_excel("employee3.xlsx", sheet_name="employee_data",engine="openpyxl")
print(df)
