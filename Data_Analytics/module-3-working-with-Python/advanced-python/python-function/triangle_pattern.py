# n = 5
# for i in range(1, n + 1):
#     for j in range(i):
#         print("* ", end="")
#     print() # for next line or moved next line


n=5
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end ="")
    print()