"""

what is single inheritance ? 

 A one parent class access by its only one child class i.e called single inheritance
 or
 
 A => B 

syntax :

class A:
   create member function 
   def __init__(self):
      body member function 

   def info(): 
      body of member function 

class B(A):
    member function():
       
obj=B()
call the method


"""

class A: 
    # constructor
    def __init__(self,name):
        self.name=name
        
class B(A):
    def __init__(self,name,address):
        super().__init__(name)   # Call A's constructor
        self.address=address
                
        
obj=B("Brijesh","150 feet ring road rajkot")
print(obj)
print(obj.name)
print(obj.address)