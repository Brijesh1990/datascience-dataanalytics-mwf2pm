import clc 
print("\n ##### choice for calculations #####")
print("\n 1. additions")
print("\n 2. substractions")
print("\n 3. Multiplications")
print("\n 4. Divisions")

while(True):
    choice=int(input('Enter a choice :'))
    if choice==1:
        print(clc.ad("a","b"))
    elif choice==2:
        print(clc.subs("a","b"))
        
    elif choice==3:
        print(clc.mult("a","b"))
        
    elif choice==4:
        print(clc.dv("a","b"))
    else:
        print("In valid choice selected")
        break;
        
       
     
    