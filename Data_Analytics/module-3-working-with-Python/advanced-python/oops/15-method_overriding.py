# method overriding ? 
# method overriding is performed any operation or task using same function pass with same arguments i.e called method overriding

class display1():
    def info(self,a,b):
        print(a)
        print(b)
        
class display2(display1):
    def info(self,a,b,c,d):
        print(a)
        print(b)
        print(c)
        print(d)
        # performed operations
        a+=b # 30
        print("Additions of numbers ",a)
        a*=b # 30*20 =600
        print("Multiplications of numbers is :",a)
    
obj=display2()
obj.info(10,20,30,40)