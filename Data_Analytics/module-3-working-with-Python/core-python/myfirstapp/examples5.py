# examples of list 
employees=["brijesh","sachin","rahul","rohit","faiz","pranav","forum","astha","mishri","sneha"]

# print list
print(employees)
print(employees[2])
print(employees[0:5])
print(employees[-1])
# lenth of list
print(len(employees))

# add new items in list
employees.append("kumar")
print(employees)

# remove an items from list
employees.remove("forum")
print(employees)

# update an items from list
employees[1]="sachin tendulkar"
print(employees)


# update rohit to rohit sharma
employees[3]="rohit sharma"
print(employees)


# update faiz to irfan khan
employees[4]="irfan khan"
print(employees)