# for i in range(1,7):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(1,7):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# square pattern 
# for i in range(6):
#     for j in range(6):
#         print("*", end="")
#     print()


# for i in range(6):
#     for j in range(6):
#         j+=1 # j=j+1
#         print(j, end="")
#     print()


# while :

# i=1
# while i<=10:
#     print(i,end="\n")
#     i+=1


# i=10
# while i>=1:
#     print(i,end="\n")
#     i-=1


# w.a.p to print multiplications of  tables 

# num=int(input("Enter your Numbers :"))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)


# w.a.p of sum of numbers 1 to 100
# s=0
# for i in range(1,101):
#     s=s+i 
#     print("s=",s)

# s=0
# for i in range(1,101):
#     s=s+i 
# print("s=",s)
 
 
#  w.a.p to reverse a string
# text=input("Enter your string :")
# rev=""
# for char in text:
#     rev=char + rev
# print(rev)

# find the sum of list of elements
# numbers=[1,15,3,56,45,25,15]
# total=0
# for num in numbers:
#     total +=num # total=num+total // 0=0+1 =1
# print(total)


# check password and login auth
em='admin@gmail.com'
pwd='admin@123'

# 3 consecutive password wrong the account blocked

for attempt in range(1,4):
    em=input("Enter your email :")
    pwd=input("Enter your password :")
    
    if em=='admin@gmail.com' and pwd=='admin@123':
        print('you are logged in successfully')
        break 
    else:
        print('your email and password are incorrect try again')
    
else:
    print('Your account is blocked due to 3 attempted failed')

 