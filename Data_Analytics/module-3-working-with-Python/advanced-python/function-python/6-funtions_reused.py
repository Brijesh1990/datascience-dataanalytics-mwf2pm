# reused function 
def ad(a,b):
     a=int(input('Enter a number :'))
     b=int(input('Enter b number :'))
     return a+b 

def subs(a,b):
    a=int(input('Enter a number :'))
    b=int(input('Enter b number :'))
    return a-b

def mult(a,b):
    a=int(input('Enter a number :'))
    b=int(input('Enter b number :'))
    return a*b 

def dv(a,b):
    a=int(input('Enter a number :'))
    b=int(input('Enter b number :'))
    return a/b 
    
 
print("\n ##### choice for calculations #####")
print("\n 1. additions")
print("\n 2. substractions")
print("\n 3. Multiplications")
print("\n 4. Divisions")

while(True):
    choice=int(input('Enter a choice :'))
    if choice==1:
        print(ad("a","b"))
    elif choice==2:
        print(subs("a","b"))
        
    elif choice==3:
        print(mult("a","b"))
        
    elif choice==4:
        print(dv("a","b"))
    else:
        print("In valid choice selected")
        break;
        
       
     
    