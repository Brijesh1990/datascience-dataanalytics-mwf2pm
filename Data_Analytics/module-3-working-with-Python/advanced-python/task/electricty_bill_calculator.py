units=int(input("Enter your unit that is used by you : "))
if units<=100:
    res=(units*5)
elif units<=200:
    res=(100*5)+(units-100)*7
elif units <=300:
    res=(100*5)+(100*7)+(units-200)*10
elif units >300:
    res=(100*5)+(100*7)+(100*10)+(units-300)*20
    
print(res)