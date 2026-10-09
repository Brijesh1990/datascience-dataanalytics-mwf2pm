# write a programme to find compund interest
p=float(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
n=float(input("Enter the time period in years: "))

# calculate compound interest
compound_interest = p * (1 + r / 100) ** n - p

print("The compound interest is:", compound_interest)