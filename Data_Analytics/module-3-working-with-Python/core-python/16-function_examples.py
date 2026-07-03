# w.a.p to print name via function 
# def name():
#     nm="my name is faiz"
#     print(nm)
# name()


# functions 
# def name():
#     nm=input("Enter your name  :")
#     print(nm)
# name()

# function return a values 
# def add():
#     a=10
#     b=20
#     c=a+b
#     return c    
# print(add())


# # pass a single parameter 

# def fullname(fname):
#     return fname
# print("My firstname is :",fullname("brijesh kumar pandey"))


# multiple arguments

# def fullname(fname,lname,age):
#     return fname,lname,age
# print("Full descriptions  :",fullname("Brijesh","pandey",35))

def fullAdd(fnm,lnm,age):
    firstname="My firstName is :"+fnm+"\n"
    lastname="My lastName is :"+lnm+"\n"
    age="My age is :",age
    print(firstname,lastname,age)

fullAdd("Brijesh","pandey",35)    

    