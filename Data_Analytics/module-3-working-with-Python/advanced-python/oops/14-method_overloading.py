# method overloading ? 
# method overloading is performed any operation or task using same function pass with different arguments i.e called method overloading

class display1():
    def info(self,a=None,b=None,c=None):
        if a is not None:
            print(a)
        if b is not None:
            print(b)
        if c is not None:
            print(c)
class display2(display1):
    pass 
obj=display2()
obj.info(10,20,30)