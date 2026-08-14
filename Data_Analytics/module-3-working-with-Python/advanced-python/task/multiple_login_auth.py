# print choice with login as 
print("======press 1 login as customers ========")
print("======press 2 login as admin ========")
print("======press 3 login as manager ========")
print("======press 4 login as employee ========")
print("======press 5 login as counceler ========")

# check 
while True:
    choice=int(input("Enter Login with As :"))
        
    if choice==1:
        email=input("Enter your email * :")
        password=input("Enter your password * :")    
        if email=='customer@gmail.com' and password=='customer@123':
            print("You are Logged in as customers successfully")
        else:
            print("Your credentials is invalid")
        
    elif choice==2:
        email=input("Enter your email * :")
        password=input("Enter your password * :")    
        if email=='admin@gmail.com' and password=='admin@123':
            print("You are Logged in as Admin successfully")
        else:
            print("Your credentials is invalid")
        
    elif choice==3:
        email=input("Enter your email * :")
        password=input("Enter your password * :")    
        if email=='manager@gmail.com' and password=='manager@123':
            print("You are Logged in as manager successfully")
        else:
            print("Your credentials is invalid")
    elif choice==4:
        email=input("Enter your email * :")
        password=input("Enter your password * :")    
        if email=='employee@gmail.com' and password=='employee@123':
            print("You are Logged in as employee successfully")
        else:
            print("Your credentials is invalid")
    elif choice==5:
        email=input("Enter your email * :")
        password=input("Enter your password * :")    
        if email=='counceler@gmail.com' and password=='counceler@123':
            print("You are Logged in as counceler successfully")
        else:
            print("Your credentials is invalid")
        
    else:
        print('selected wrong choice')
        break;
        
          
          
    
   