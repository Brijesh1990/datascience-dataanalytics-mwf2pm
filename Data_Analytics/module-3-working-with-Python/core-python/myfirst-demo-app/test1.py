# input from users 

principle = float(input("Enter the principle amount: "))

rate = float(input("Enter the rate of interest: "))

time = float(input("Enter the time period: "))


simple_interest = (principle * rate * time) / 100

print("The simple interest is:", simple_interest)