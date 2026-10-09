#find a canteen food wastage managements systems 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

# create a food list 
food_menu={
    "food_name":["sandwich","burger","pizza","rotli","salad","pav bhaji","magi","pepsi","dosa","samosa","tea","cofi"],
    
    "wastage":[50,10,100,25,15,25,30,45,78,25,90,25]
}

# create a dataframes 
df=pd.DataFrame(food_menu)
# create tabular layout
print(df)

# find total sum of wastage 
print("----------------------")
sum_wastage=df["wastage"].sum()
print("Total of food wastage :",sum_wastage,"kg")
# find average of wastage
print("----------------------")
avg_wastage=df["wastage"].mean()
print("Average of food wastage :",avg_wastage, "kg")
# find max wastage of food 
print("----------------------")
max_wastage=df["wastage"].max()
print("Max wastage of food  :",max_wastage, "kg")
# display in pi chart 
plt.title("max wastage Food Name Data")
plt.figure("16x12")

plt.pie(
    
    df["wastage"],
    labels=df["food_name"],
    colors=["#7d7f82","#0db002","#d10011","#2ea1c7","#c1c5c7","#3b87ad","#b8b440","#a978ab","#a978ab","#84a8c4","#ae68b3","#540913"],
    autopct="%1.1f%%",
    startangle=90
        
)
plt.show()

