try:
    with (open("C:\\Namaste React\\Namaste React All Asssigments\\Episode 03 - Laying the Foundation\\Assignment.md") as
          file):
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("File Not Found")
