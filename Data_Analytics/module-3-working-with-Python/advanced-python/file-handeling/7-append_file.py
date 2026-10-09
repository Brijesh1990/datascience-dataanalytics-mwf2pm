# with open("brijesh_portfolio.txt", "a") as file:
#     txt = "\n This is Brijesh .\n I am 35 years of old."
#     file.write(txt)


with open("brijesh_portfolio.txt", "r+") as file:
    print(file.read())
    