file=open("module.txt","w")
if file:
    print("file is opened successfully")
else:
    print('something went wrong while open file')
    
file.close()    
