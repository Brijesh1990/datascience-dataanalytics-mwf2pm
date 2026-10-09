# with is closed file automatically after the block of code is executed
# with open("modes_txt.txt", "r") as file:
#     modes = file.mode
#     print(modes)


with open("modes_txt.txt", "w") as file:
    modes = file.mode
    
    print(modes)
    