temp = float(input("What is the temperature outside: "))

if temp >= 0 and temp <= 35.5:
    print("The temperature is good today\nGo Outside!")

elif temp < 0 or temp > 40:
    print("The temperature is bad today\nStay Inside!")
