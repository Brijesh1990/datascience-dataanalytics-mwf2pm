import os
path = "examples.txt"
try:
    os.remove(path)
    print("File removed successfully")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")