import os
import shutil

path = "test_folder"

try:
    # os.remove(path)        # delete a file
    # os.rmdir(path)         # delete an empty directory
    shutil.rmtree(path)    # delete a directory containing files

except FileNotFoundError as e:
    print(e)
    print(f"{path} not found")

except PermissionError as e:
    print(e)
    print("You don't have permission to delete folder")

except OSError as e:
    print(e)
    print("this is not an empty directory")
