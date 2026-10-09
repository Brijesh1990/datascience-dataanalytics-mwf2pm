
class App():
        print("\n=======Enter 1 for additions :====")
        print("\n=======Enter 2 for substractions :====")
        print("\n=======Enter 3 for Multiplications :====")
        print("\n=======Enter 4 for Exit :====")
        def __init__(self,choice,a,b):
            self.choice=choice
            self.a=a 
            self.b=b
            
            if self.choice==1:
                print("Additions of numbers is :",self.a+self.b)
            elif self.choice==2:
                print("Subs of numbers is :",self.a-self.b)
            elif self.choice==3:
                print("Multiplications of numbers is :",self.a*self.b)
            
                
while True:
    choice=int(input("Enter your choice :"))
  
    if choice >=4:
        print("wrong choice selected")
        break

    a=int(input("Enter a Numbers :"))
    b=int(input("Enter b Numbers :"))
    # create an object of class App to access class properties 
    obj=App(choice,a,b)
    
                
             
    
      