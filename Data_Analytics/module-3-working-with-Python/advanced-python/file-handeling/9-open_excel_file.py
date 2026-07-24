# with open('workbook1.xlsx','r+') as file:
#     print(file.read())

# pandas read content excel or csv
# read a excel content using third party module pandas 

# import pandas as pd 
# df=pd.read_excel("workbook1.xlsx")
# print(df)


# read excel content workbook of particular sheet

import pandas as pd 
df=pd.read_excel("workbook1.xlsx", sheet_name="attendanace")
print(df)