"""
what is block statements or conditional statements 
  conditional statements check true and false
  
  types of conditions statements 
  
  1) if 
  2) if else 
  3) nested if 
  4) if elif
  5) switch 


 types of looping statements ...
 
 where check numbers of iterations again and again there we used loop    
 or
 where print numbers of iteration repeated more than one time there we used loop   
 
 types of loop 
 
 a) for
 b) while 
 c) do while
    
"""

# conditional statements 

# if statements :
# if is executed when condition is true 
# syntax 
# if condition:
#  statements
# example of if statements 
# a=10
# b=20
# if a>b:
#   print("a is greater than b") 

# a=40
# b=20
# if a>b:
#   print("a is greater than b") 

# a=int(input("Enter a Numbers : "))
# b=int(input("Enter b Numbers : "))
# if a>b:
#   print("a is greater than b") 


# if else : if executed when conditions i true if condition is false else is executed 

# syntax 

# if condition:
#   statements
# else:
#   statements

# examples ...

# a=int(input("Enter a Numbers : "))
# b=int(input("Enter b Numbers : "))
# if a>b:
#   print("a is greater than b")
# else:
#   print("a is less than b")
 
 
 
#  nested if : if within another if or condition within another conditions there we used nested if statements 

# syntax 

# if condition:
#   if condition:
#     statements
# else:
#   statements 

# examples : 
# a=int(input("Enter a Numbers : "))
# b=int(input("Enter b Numbers : "))
# if a>b:
#   if a!=0 and b!=0:
#     print("a is greater than b and both are positive numbers")
# else: 
#   print('a is less than b')
 
 
 
# if elif : if elif used to check multiple true conditions if is true it executed and elif check multiple true conditions if elif false else is executed

# n1=int(input("Enter N1 Numbers : "))
# n2=int(input("Enter N2 Numbers : "))
# n3=int(input("Enter N3 Numbers : "))

# if n1>n2 and n1>n3:
#   print("N1 is max Numbers")
# elif n2>n1 and n2>n3:
#   print("N2 is max Numbers")
# elif n3>n1 and n3>n2:
#   print("N3 is max Numbers")
# else:
#   print('something went wrong')



# switch : switch case is not supported in python 
  
# w.a.p to check a number is even or odd take input from users..................
 
# number=int(input("Enter a numbers :"))
# # check number odd | even 
# # number/2 modulas zero number is even if modulas not zero odd    
# if number%2==0:
#   print('A number is even')
# else: 
#   print('A number is odd')     

# w.a.p to check if age >=18 so eligible for voting if age<=18 not eleible for voting
# age=int(input("Enter your age :"))
# # check age 
# if age>=18:
#   print('eligible for voting')
# else:
#   print('not eligible for voting')


# w.a.p to enter three subject marks and find grade 
# math=int(input("Enter math marks :"))
# science=int(input("Enter science marks :"))
# chemistry=int(input("Enter chemistry marks :"))

# res=(math+science+chemistry)/3

# if res>=75:
#   print("you are toppers students")
# elif res>=60:
#   print("you are first divisions students")
# elif res>=45:
#   print("you are second divisions students")
# elif res>=33:
#   print("you are Third divisions students")
# else:
#   print("You are failed students")



#w.a.p to create a simple calculator to perform additions while user press 1, and press 2 substractions , press 3 multiplcations and 4 divisions if press 5 proggrame exit

print("########select choice #########")
print("press 1 for additions")
print("press 2 for substractions")
print("press 3 for multiplications")
print("press 4 for divisions")
while True:
  number=int(input('Enter your choice ....'))
  if number==1:
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a+b
    print("Additions of numbers is :",c)
    break
  elif number==2:
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a-b
    print("Substractions of numbers is :",c)
    break
  elif number==3:
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a*b
    print("Multiplications of numbers is :",c)
    break  
  elif number==4:
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a/b
    print("Divisions of numbers is :",c)
    break
  else:
    print("sorry you selected wrong choice")
    break

   