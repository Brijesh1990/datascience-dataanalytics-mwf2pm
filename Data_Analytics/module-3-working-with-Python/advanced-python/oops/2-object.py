"""
what is object ? 

  1. An object is an instances of class
  2. An object is an examples of class 
 
  syntax of class 
  
  class className:
      body of class
      create a function:
           body of member function

  create an object of class
  call a member function 
  

"""

class Car:
    name="Alto 800"
    def __init__(self,carname,price,years):
        self.carname=carname 
        self.price=price 
        self.years=years 
    
obj=Car("Mercedes","480000","2026") # Car() is an object of class Car 
print("Car name is :",obj.name)
print("Car Price is :",obj.price)
print("Car Manufacturing years is :",obj.years)
        
