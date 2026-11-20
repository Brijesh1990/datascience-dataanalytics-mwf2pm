# series is an inbuilt method in python used pandas 
# series is used to provides data of one column
import pandas as pd 
data={
    "id":[1,2,3,4,5],
    "name":["faiz","meet","mathur","mishri","forum"],
    "age":[21,22,23,24,25],
    "salary":[21000,22000,23000,24000,25000]   
}

df=pd.Series(data)
print(df)
