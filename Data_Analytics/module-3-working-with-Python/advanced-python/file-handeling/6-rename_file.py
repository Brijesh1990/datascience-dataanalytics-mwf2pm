import os
path = "examples1.txt"
try:
    os.rename(path, "brijesh_portfolio.txt")
    print("File renamed successfully")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")