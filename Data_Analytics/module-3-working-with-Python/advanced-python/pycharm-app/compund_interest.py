import math
p=int(input('enter principle ammount :'))
r=int(input('enter rate of interest :'))
n=int(input('enter number of years :'))

ci=p * (math.pow((1 + r / 100), n))
print("compund interest is :",ci)


