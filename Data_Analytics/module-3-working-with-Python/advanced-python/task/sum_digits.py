num=int(input("Enter a Numbers :"))
total=0
#12
while num > 0:
    digit=num % 10 # 2
    total+=digit   # 2  total=total + digit  
    num=num // 10  # remove last digit 1
print("sum of digits :",total) 
    