# import datetime
# print(datetime.datetime.now())

# from datetime import datetime
# print(datetime.now())

# from datetime import datetime
# print(datetime.date())

# from datetime import datetime
# current_day=datetime.now()
# print("Today the day name is :",current_day.strftime("%A"))
# print("Today the years is :",current_day.strftime("%Y"))
# print("Today the date is :",current_day.strftime("%F"))
# print("Today the date is :",current_day.strftime("%d/%m/%Y"))
# print("Today the date is :",current_day.strftime("%d.%m.%Y"))
# print("Today the date is :",current_day.strftime("%d-%m-%Y"))
# print("Today the month name is :",current_day.strftime("%B"))

# calendar 

# import calendar
# print(calendar.calendar(2026))


# july month calendar 
# from calendar import calendar
# print(calendar(2026))


# import calendar
# print(calendar.month(2026,7))

# import sys
# print("python major version :",sys.version_info)


# import platform
# print("python  version :",platform.python_version())

# give a floor values 
# import math
# res=math.floor(145.166565656)
# print(res)


# import math
# number=16
# res=math.pow(number,2)
# print(res)

# pandas dataFrame 
import pandas as pd
employee={
    
    "fname":["faiz","forum","kumar"],
    "age":[21,22,23],
    "salary":[15500,16500,17500]
    
}

df=pd.DataFrame(employee)
print(df)

