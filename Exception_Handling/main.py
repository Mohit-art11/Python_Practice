try:
    numerator = float(input("Enter a number to divide: "))
    denominator = float(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero")

except ValueError as e:
    print(e)
    print("You can't divide by string")

else:
    print(result)