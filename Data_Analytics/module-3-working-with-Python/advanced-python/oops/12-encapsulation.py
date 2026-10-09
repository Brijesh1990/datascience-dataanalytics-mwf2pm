# encapsulation is used to wrap up a data in single object i.e called encapsulation
# data access in encapsulation by access modifier or private | public | protected

# encapsulation is used  for visibility of data via 

#   private | public | protected

# public : accessible anywhere i.e public 
# class employee:
#     def __init__(self,name):
#         self.name=name #accessible via public
#         # create a public method
#     def display_em(self):
#         print(self.name)

# obj=employee("brijesh")
# obj.display_em() #accessible via public
# print(obj.name)  #accessible anywhere
            
    
# private :that can be accessible only inside of class i.e called private

# class employee:
#     def __init__(self,name):
#     # public attributes
#         self.name=name
#     # public method 
#     def show_age(self,age):
#         print(age)
#     # private method
#     def show_address(self):
#         print("Address is :",self.__address)
        
# # create an object 
# obj=employee("Brijesh")
# print(obj.name)  # accessible name
# obj.show_age(35) # accessible
# obj.show_address("150 feet ring road") #not accessible due to this is a private
# print(obj.__address)


# protected : when method is protected it should be accessible only by its one child class 

class employee:
    # public attributes
    def __init__(self,name,age):
        self.name=name 
        self.age=age

# call protected method
class subemployeedetails(employee):
    def show_age(self):
        print("Employee name is :",self.name)
        print("Employee age is :",self.age)

obj=subemployeedetails("brijesh kumar pandey",35)
obj.show_age() # accessible because of this is protected
    
        
   
        
    
 