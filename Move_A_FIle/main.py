import os

source = "index.html"
destination = "C:\\Users\\91907\\Music\\index.html"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(f"{source} has moved")

except FileNotFoundError as e:
    print(e)
    print(f"{source} not found")
