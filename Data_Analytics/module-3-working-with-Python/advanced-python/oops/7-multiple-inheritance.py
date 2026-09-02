"""

what is multiple inheritance ? 
  A multiple derived class properties access by its one child class i.e called multiple inheritance
  python will support multiple inheritance
  
# note : python and c++ is support multiple inheritance
 
 
  A     B     C 
      
      
      D   
 
 
syntax :

class A:
  statements
  member function():
     statements
    

class B:
  statements
  member function():
     statements
     

class C:
  statements
  member function():
     statements


class D(A,B,C):
  statements
  member function():
     statements
     
//create an object
obj=D()
print(obj.properties)

"""
# class Mother:
#     mothername=""
#     def motherInfo(self):
#         print(self.mothername)
        
# class Father:
#     fathername=""
#     def fatherInfo(self):
#         print(self.fathername)


# class GrandFather:
#     grandfathername=""
#     def fatherInfo(self):
#         print(self.grandfathername)
        
# class Son(Mother,Father,GrandFather):
#     sonname=""
#     def FamilyInfo(self):
#         print("Mother name is :",self.mothername)
#         print("Father name is :",self.fathername)
#         print("GrandFather name is :",self.grandfathername)
#         print("Son name is :",self.sonname)

# obj=Son()
# obj.mothername="Mrs. shashikala pandey"
# obj.fathername="Mr. Ravindra nath pandey"
# obj.grandfathername="DR. Amardev pandey"
# obj.sonname="Brijesh kumar pandey"
# obj.FamilyInfo()
    
        
        
class Mother:
    mothername=""
    # default constructor self called when create the object of class 
    def __init__(self,mothername):
        self.mothername=mothername
        print(self.mothername)
        
class Father:
    fathername=""
    def __init__(self,fathername):
        self.fathername=fathername
        print(self.fathername)


class GrandFather:
    grandfathername=""
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername
        print(self.grandfathername)
        
class Son(Mother,Father,GrandFather):
    sonname=""
    def __init__(self,fathername,mothername,grandfathername,sonname):
        self.fathername=fathername
        self.mothername=mothername
        self.grandfathername=grandfathername
        self.sonname=sonname
                
obj=Son("Mrs shishikala pandey","Mrs Ravindra nath pandey","Dr Amardev pandey","Brijesh kumar pandey")
print(obj)
print(obj.fathername)
print(obj.mothername)
print(obj.grandfathername)
print(obj.sonname)



        
        
