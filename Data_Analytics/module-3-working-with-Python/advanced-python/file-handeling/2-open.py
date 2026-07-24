# open()
# file=open("hello.txt","r")
# if file:
#     print("file is opened successfully")
# else:
#     print('something went wrong while open file')

# write mode 
file=open("hello.txt","w")
if file:
    print("file is opened successfully")
else:
    print('something went wrong while open file')
    

file.close()    

