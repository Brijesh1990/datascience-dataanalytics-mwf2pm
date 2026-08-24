""" 
A constructor is a same name of class 
or
A constructor is same name of class whenever we create an object of class constructor automatically called 

note : A constructor is a default method that can be defined as __init__(self) arguments


"""

class college:
    collegeName="T.N.Rao college"
    # create an constructor 
    def __init__(self,name,address,trustname):
        self.name=name
        self.address=address
        self.trustname=trustname

obj=college("Atmiya college","150 feet ring road near kalawad road rajkot","gurukul")
print(obj.name)
print(obj.address)
print(obj.trustname)