# **kwargs => Parameter that will pack all arguments into a dictionary

def greet(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

greet(title="Mr.", first="Shivam", last="Sharma")
