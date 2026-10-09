# what is module in python ?

- a module is an small peace of file that can be save in python using .py i.e called module.

- a module is saved with .py i.e called module in python 

- there are some types of module in python 

1. user defined module 
2. pre defined module or system defined module
3. third party module or libraries 

## user defined module 

- user defined module is defined by user save with .py file 
- examples 
- name.py
```
name=input("Enter your Name : ")
print("Your name is :",name)
``` 

## pre-defined module 

- pre-defined module is a system defined module 
- pre - defined module is used to calculate some power | math functions etc in python 
- pre defined module is used by **import keyword**

- examples of pre-defined module 

```
# import math
# print(math.factorial(25))

# import math
# print(math.factorial(5))

# square | qube 
# import math
# print(math.pow(4,2))
# print(math.pow(2,3))
# print(math.pow(6,2))
# print(math.pow(5,3))
# sqrt  25=5
# import math
# # print(math.sqrt(25))
# print(math.floor(12.3656))


# print calendar 
import calendar
# 2026
# print(calendar.calendar(2026))
# 2026 of june month
# print(calendar.month(2026,6))
print(calendar.month(2008,8))

import random
# otp generate 4 number 
print(random.randint(1111,9999))

# otp generate 6 digit 
print(random.randint(111111,999999))

# otp generate 8 digit 
print(random.randint(11111111,99999999))

```

## third party module or libraries 

- third party module is used to in package formate 
- third party module is always installable 
- third party module install with **pip**
- pip stands for **python install package** 

# note : create a programme of DataFrame and show employee details in data frames with tabular layout

**examples**
```
import pandas as pd
employee={
"fname":["faiz","forum","pranav","astha","brijesh","mishri"],

"lname":["sumra","unadkat","mathur","solanki","patel","pandey"]
}
print(pd.DataFrame(employee))

```




