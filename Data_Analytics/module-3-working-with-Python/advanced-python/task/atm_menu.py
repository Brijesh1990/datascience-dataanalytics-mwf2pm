balance=50000
while True:
    print("\n -----ATM Menu------")
    print("\n 1. check The balance of account")
    print("\n 2. Deposit")
    print("\n 3. withdrawl ")
    print("\n 4. exit")
    
    choice=int(input("Enter your choice :"))
    if choice==1:
        print("Your account balance is :",balance)
    elif choice==2:
        ammount=int(input("Enter a deposit ammount :"))
        balance+=ammount #
        print("Your balance is :",balance)
        
    elif choice==3:
        ammount=int(input("Enter a withdrwal ammount :"))  
        if ammount<=balance:
             balance-=ammount
             print("Your remaining balance is :",balance)
            
        else:
            print('Insufficient balanace')
        
    elif choice==4:  
        break

    else:
        print('select wrong choice') 
    
        