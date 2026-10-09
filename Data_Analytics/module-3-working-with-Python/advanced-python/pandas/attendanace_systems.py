# create a data frames 
import pandas as pd 
import matplotlib.pyplot as plt 

data = {
    "studentname": ["Faiz", "Jay", "Meet", "forum", "rutwick", "brijesh","astha","pranav"],
    "attendance": [0, 0, 1, 0, 0, 0,0,0]
    
}

# print in dataframes 
df=pd.DataFrame(data)
print(df)

# display absent and present values 

present=(df["attendance"]==1).sum()
absent=(df["attendance"]==0).sum()

# data visualized values 

label=["Present","Absent"]
values=[present,absent]
colors=["green","red"]

# display chart 
plt.pie(
    values,labels=label,  autopct="%1.1f%%", colors=["green","red"]
)
plt.show()