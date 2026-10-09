# banks details
name="axis bank of India pvt Ltd"
pin="123456"
user="pranav mathur"
balance="480000"
while True:
    print("#### select Menu ####")
    print('\n select 1 for bank details')
    print('\n select 2 for Pin')
    print('\n select 3 for account holder user name')
    print('\n select 4 for account balance')
   
    choice=input("Enter your choice :") 
    if choice=="1":
        pincode=input("Enter your pin :")
        if pincode==pin:
            print((f"Your account is 🏠 {name}"))
        else:
            print("entered wrong pin numbers")
    elif choice=="2":
        pincode=input("Enter your pin :")
        if pincode==pin:
            print((f"Your pin numbers is 📌 {pin}"))
        else:
            print("entered wrong pin numbers")
            
    elif choice=="3":
        pincode=input("Enter your pin :")
        if pincode==pin:
            print((f"Your account holder Name   is 👤 {user}"))
        else:
            print("entered wrong pin numbers")
    
    elif choice=="4":
        pincode=input("Enter your pin :")
        if pincode==pin:
            print((f"Your account balance is  💲 {balance}"))
        else:
            print("entered wrong pin numbers")
    else:
        print("you select wrong choice try again")
        break
        
        
        
            
            