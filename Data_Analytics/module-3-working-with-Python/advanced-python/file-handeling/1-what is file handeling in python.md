# what is file handling in python ?

1. File handling in Python refers to the process of reading from and writing to files.

2. It allows you to interact with files on your computer, enabling you to store and retrieve data persistently.

3. file handling is used to read | write data to files, which can be useful for tasks such as logging, data storage, and configuration management.

4. file handling also read | write on text files, binary files, csv, excels and other file formats.

5. Python provides built-in functions and methods for file handling, making it easy to work with files in a variety of formats...

## types of file handling functions in python

- `open()`: Opens a file and returns a file object.
- `read()`: Reads the contents of a file.
- `write()`: Writes data to a file.
- `close()`: Closes an open file.
-  with the `with` statement, you can automatically close files after their suite finishes, even if an exception is raised.
- `seek()`: Moves the file pointer to a specific position in the file.
- `tell()`: Returns the current position of the file pointer.
- `flush()`: Flushes the internal buffer, ensuring that all data is written to the file.
- `readline()`: Reads a single line from the file.
- `readlines()`: Reads all lines from the file and returns them as a list.
- `writelines()`: Writes a list of strings to the file.
- `truncate()`: Truncates the file to a specified size.
- `os.remove()`: Deletes a file from the filesystem.
- `os.rename()`: Renames a file in the filesystem.
- `os.path.exists()`: Checks if a file exists in the filesystem.
- `os.path.getsize()`: Returns the size of a file in bytes. 
- `os.path.abspath()`: Returns the absolute path of a file.
- `os.path.basename()`: Returns the base name of a file (the file name without the directory path).
- `os.path.dirname()`: Returns the directory name of a file (the path without the file name).


## mode in file handling in python

**r**: Read mode - Opens a file for reading (default mode). The file pointer is placed at the beginning of the file. If the file does not exist, it raises a FileNotFoundError.

**r+**: Read and Write mode - Opens a file for both reading and writing. The file pointer is placed at the beginning of the file. If the file does not exist, it raises a FileNotFoundError.

**w**: Write mode - Opens a file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.

**w+**: Write and Read mode - Opens a file for both writing and reading. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.

**a**: Append mode - Opens a file for appending. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.

**a+**: Append and Read mode - Opens a file for both appending and reading. The file pointer is placed at the end of the file. If the file does not exist, it creates a new file.


## how to get mode of file in python

   **Example:**
  ```
    with open("modes_python.txt","r") as file:
      print(file.mode)
    
    or

    file = open("example.txt", "r")
    print(file.mode)
    file.close()

  ```

# how to read a file of excel in python
# install pandas library using pip install pandas

