import os

file_path = "C:\\Users\\91907\\Desktop\\os_folder"

if os.path.exists(file_path):
    print("That's location exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print("That's location doesn't exist")
