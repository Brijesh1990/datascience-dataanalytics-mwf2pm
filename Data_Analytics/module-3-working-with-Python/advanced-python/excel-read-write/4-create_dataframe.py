import pandas as pd 
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