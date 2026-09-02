"""

what is multilevel inheritance ? 

 A one parent class access by its  child class and its again access its child class properties i.e called multilevel inheritance
 or
 
 A => B => C => D

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
    
class C(B):
    def __init__(self,name,address,department):
        super().__init__(name,address)   # Call A's constructor
        self.department=department
                

        
obj=C("Brijesh","150 feet ring road rajkot","Computer science")
print(obj)
print(obj.name)
print(obj.address)
print(obj.department)