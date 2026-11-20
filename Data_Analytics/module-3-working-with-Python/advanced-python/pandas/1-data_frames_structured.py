import pandas as pd 

data={
    "id":[1,2,3,4,5],
    "name":["faiz","meet","mathur","mishri","forum"],
    "age":[21,22,23,24,25],
    "salary":[21000,22000,23000,24000,25000]   
}
df=pd.DataFrame(data)
# print(df)
print(df)
# find the max salary data 
print("maximum salary in dataframes ",df["salary"].max())
# find the min salary data
print("minimum salary in dataframes ",df["salary"].min())
# find the average salary data 
print("Average  salary in dataframes ",df["salary"].mean())
# find the sum of salary data 
print("Total sum of salary in dataframes ",df["salary"].sum())
print(type(df))
