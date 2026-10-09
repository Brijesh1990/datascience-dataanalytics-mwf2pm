import pandas as pd
employee_data={
    
    "name":["faiz","brijesh","paranav","astha","sneha","forum"],
    "age":[23,24,25,26,27,28],
    "salary":[10000,20000,30000,40000,50000,60000],
    "department":["IT","HR","Finance","Marketing","Sales","Operations"]
}

df=pd.DataFrame(employee_data)
print(df)
# find the length of the dataframe
length=len(df)
print("Length of the dataframe:", length)
# update forum to  jinal
dfupd=df.replace("forum","jinal")
print(dfupd)
# delete the jinal from dataframes 
delData=dfupd[dfupd.name!="jinal"]
print(delData)
# print the data frames 
print(employee_data)
print(df)