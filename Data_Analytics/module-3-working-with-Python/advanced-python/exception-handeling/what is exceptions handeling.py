# what is exceptions handling in python ?
# An exception handling is an block execution inside of python that can be find exception inside of code using 

# try:
#     statements

# except:
    
#     statements
    
# finally:
    
#     statements


# a=10
# b=20
# c=a+b 
# try:
#     print("Additions of numbers :",c)
# except:
#     print('something went wrong')
    


# x=10 
# try:
#     print("THe values of x is :",y)
# except:
#     print('something went wrong')
    
    

# a=int(input("Enter a values :"))
# b=int(input("Enter a values :"))
# try:
#     if a>b:
#         print("a is greater than b")
#     else:
#         print("a is smaller than b")
# except:
#     print("something went wrong")




# finally :

# a=int(input("Enter a values :"))
# b=int(input("Enter a values :"))
# try:
#     if a>b:
#         print("a is greater than b")
#     else:
#         print("a is smaller than b")
# except:
#     print("something went wrong")
    
# finally:
#     print("everything work fine")


try:
    class A:
        def __init__(self,name,age):
            self.name=name
            self.age=age
         
except:
    print("something went wrong")
obj=A("brijesh",35)
print(obj)
print(obj.name)
print(obj.age)
        