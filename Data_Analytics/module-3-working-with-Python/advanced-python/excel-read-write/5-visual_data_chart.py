import pandas as pd 
import matplotlib.pyplot as plt 
data={
    "name":["paranav","faig","meet","astha","forum"],
    "age":[21,22,23,24,25],
    "salary":[21000,22000,24000,25000,26000]
}

# create a dataframe
# create tabular layout 
# create a structured data 
# provides default index or row 
df=pd.DataFrame(data)
print(df)
# visualized data using matplotlib library 
# plt.pie(df["age"],labels=df["name"],  autopct="%1.1f%%")
# plt.title("employee data with age")
# plt.show()

# create a bar char
plt.bar(df["name"],df["age"])
plt.title("age of employee")
plt.show()
