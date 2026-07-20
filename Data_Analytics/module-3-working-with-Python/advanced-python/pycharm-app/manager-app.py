# create a manager app
#print("Hello World")
# w.a.p to find a compund interest
p=int(input('enter principle ammount :'))
r=int(input('enter rate of interest :'))
#n = 12 # Compounded monthly
n=int(input('enter number of years :'))
# formula of compond interest
amount = p * (1 + r / 100) ** (n)
# 2. Calculate compound interest alone
interest = amount -p

print(f"Total Amount: Rupees{amount:.2f}")
print(f"Interest Earned: Rupees{interest:.2f}")