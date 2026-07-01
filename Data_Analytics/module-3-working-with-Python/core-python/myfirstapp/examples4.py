import pandas as pd

employees = {
    
    'Name': ['John', 'Alice', 'Bob', 'Eve'],
    'Age': [28, 34, 22, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing'],
    'salary': [50000, 60000, 55000, 70000],
    'Joining Date': ['2020-01-15', '2019-03-22', '2021-07-10', '2018-11-05']
}

print(pd.DataFrame(employees))