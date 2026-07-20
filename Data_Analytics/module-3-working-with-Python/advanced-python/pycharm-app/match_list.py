employee=["mishri","faiz","forum","brijesh","astha","pranav"]

# match a faiz is available of not
# if employee[1]=='faiz':
#     print("faiz is vailable")
# else:
#     print("faiz is not vailable")

inp=input("Enter employee Name :")

# match name from list anc check av ailabilty

if inp in employee:
    print("Employee Name Exists or avialable")
else:
    print("Employee Name is Not Exists or not available")