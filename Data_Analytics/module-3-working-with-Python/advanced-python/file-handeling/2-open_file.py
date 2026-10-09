# open and close file using open() and close() method

# file=open("examples.txt","r")
# if file.mode=="r":
#     contents=file.read()
#     print(contents)
# file.close()


# file=open("examples.txt","w")
# if file.mode=="r":
#     contents=file.read()
#     print(contents)
# file.close()




file=open("examples1.txt","w")

if file:
    print("File opened successfully")
else:
    print("File not opened successfully")
file.close()