import logic_app
print("##########select your  choice###########")
print('''
      select 1 for additions 
      select 2 for substractions
      select 3 for multiplications
      select 4 for divisions
      select 5 for modulas
      select 6 for exit
      
      ''')

while True: 
    # choice based 
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))    
    
    choice=int(input("Enter your choice "))
    if choice==1:
        print(logic_app.add(a,b))
    elif choice==2:
        print(logic_app.subs(a,b))
    elif choice==3:
        print(logic_app.mult(a,b))
    elif choice==4:
        print(logic_app.dv(a,b))
    elif choice==5:
        print(logic_app.mod(a,b))
    else:
        print("you select wrong choice")
        break     