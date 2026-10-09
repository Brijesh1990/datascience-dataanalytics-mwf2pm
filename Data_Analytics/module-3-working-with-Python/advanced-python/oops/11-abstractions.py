# abstract class is hide some internal data from some users 
# abstract is used for hiding data 
# when we create a class as abstract we never create its object
# we access abstract class by another class 

from abc import ABC,abstractclassmethod
class Greet:
    @abstractclassmethod 
    def say_hello(self):
        return 'my name is abstract'
class English(Greet):
    def say_hello(self):
        return 'hello Greet'
    
obj=English()
print(obj.say_hello())
        