# w.a.p to count any even and odd numbers in given list

# number=[10,15,16,20,25,35,40,1,13]
# even=0
# for i in number:
#     if i%2==0:
#         even+=1 
# print(even)
    
    
# number=[10,15,16,20,25,35,40,1,13]
# even=0
# for i in number:
#     if i%2!=0:
#         even+=1 
# print(even)
    
    
    
number=[10,15,16,20,25,35,40,1,13]
even=0
odd=0
for i in number:
    if i%2==0:
        even+=1
    else:
        odd+=1
             
print("Number of even numbers in list ",even)
print("Number of od numbers in list ",odd)
        
