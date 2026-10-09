"""
what is class ? 

  1. A class is nothing whenever we can not create its object
  2. A class is group of its member and member function
  3. A class is blue print or shadow of  it's object 

  syntax of class 
  
  class className:
      body of class
      create a function:
           body of member function

  create an object of class
  

"""
class A:
    # defined an attributes of class 
    fname="brijesh kumar pandey"
    # create a constructor
    def __init__(self,fname,age):
        self.name=fname # instance of class attributes
        self.age=age    

# create an object of class A 
obj=A("brijesh",35) # A() is an object of class A
print(obj.fname)
print(obj.age)