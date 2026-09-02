file=open("examples1.txt","w")

txt="Hello, this is a sample text written to the file.\nThis is the second line of the text."

txt1="This is the third line of the text.\nThis is the fourth line of the text."

file.write(txt1)
file.write(txt)

file.close()