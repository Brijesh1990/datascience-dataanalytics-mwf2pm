# block statements 
# check true or false there we used conditional statements 
# conditional statements 
# types of conditional statements 

# if
# if else 
# nested if
# if elif
# switch(python not supported)

# if statements ...
# if condition is true then if is executed 

# syntax 

# if condition:
#     statements

# a=40
# b=20
# if(a>b):
#     print("a is greater than b")
    
    
# if else statements

# idf is executed when condition is true if condition is false else is executed 

# syntax 

# if (condition):
#     statements
# else:
#     statements

# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))

# if a>b:
#     print("a greater than b")
# else:
#     print("a smaller than b")
    
    
# single line statements or ternary operator like used it
# true and false check 

# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))

# if a>b:print("a is greater than b") 

# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))

# print("a is greater than b") if a>b else print("a is less than b")

# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))

# result="a is greater than b" if a>b else "a is lesser than b"
# print(result)


# nested if : 
# nested is used if within another if i.e called nested if statements 

# syntax 

# if condition:
#     if condition:
#         statements
# else:
#     statements
 

# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))

# if a>b:
#     if a!=0 and b!=0:
#         print("a is greater than b and both are positive")
# else:
#     print("a is less than b")


# w.a.p to check years is leap leap years 
# year=int(input("Enter a years :"))
# if year%4==0:
#     print("leap years")
# else:
#     print("not a leap years")
# w.a.p to check numbers is odd or even 
# numbers=int(input("Enter a numbers :"))
# if  numbers%2==0:
#     print("even numbers")
# else:
#     print("odd numbers")
# w.a.p to check eligible for vote or not 
# age=int(input("Enter a your age :"))
# res="eligible for vote" if age>=18 else "not eligible for voting"
# print(res)


# if elif : 
# if is executed when condition is true elif check multiple true conditions while its not false if false else is executed 

# syntax 

# # if condition:
#      statements
#   elif condition:
#       statements
#   elsif condition:
#       statements
#   else:
#       statements

    
# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))
# if a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")
# else: 
#     print("a and b both are equal") 


# marks > 75 topper > 65 > average > 55 just passed < 33 failed 

# marks=int(input("Enter your marks :"))
# if marks>=75:
#     print("i am a topper")
# elif marks>=65:
#     print("i am average students")
# elif marks >=55:
#     print("i am just passed out")
# else:
#     print("i am failed")    

# logged in systems 

# dep=input("Enter your departments :")
# if dep=='admin':
#     print("You are logged in as admin")
# elif dep=='faculty':
#     print('you are logged is as faculty')
# elif dep=='hr':
#     print('you are logged is as HR')
# else:
#     print('kindly contact with admin your credentials not found')
    
   
   
# switch not support in python    


# looping statements ?  

"""
loop statements  ? 
 loop is executed or repeated number od iteration again and again there we used loop
 
 or 
 
 loop is executed or print numbers of iteration again and again i.e called loop 
 
 types of loop in python ? 
 
  1. for()
  2. while() 
  3. do while()
  

"""
 
# for loop : for loop is executed when condition is true if false for loop is terminated 

# syntax 
# for variable in range():
#     statments

# print 1 to 100...

# for num in range(1,101):
#     print(num , end=" ")

# for num in range(1,101):
#     print(num, end="\n")
 
 
#  while : while loop is executed when condition is true 

# i=0
# while(i<=10):
#     print(i, end=" ")
#     i+=1; # i++ ; i=i+1 
      
      
# i=1
# while(i<=10):
#     print(i, end="\n")
#     i+=1; # i++ ; i=i+1



# i=10
# while(i>=1):
#     print(i, end="\n")
#     i-=1; # i-- ; i=i-1 


# do while : do will be executed once time either condition is true or false while executed when condition is true
# i=0
# do 
# {
#  print(i)
#  i+=1    
# }
# while(i<=10)

# note : do while is not supported in python


# control flow statements : 
# continue 
# break 
# pass
# yield 
 
# 1 to 9   
# for i in (1,10):
#          if i==3: 
            
 



