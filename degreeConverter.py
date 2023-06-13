degree = float(input("Please input your temperature: "))
unit = str.upper(input("Please input either C or F: "))
if unit == "C":
    converted = (float(degree) * 1.8) + 32
    print("Your temperature in F is:" + str(converted))
elif unit == "F":
    converted = (float(degree) - 32) * 0.5555555556
    print("Your temperature in C is:" + str(converted))
elif unit != "C" or unit != "F":
    print("Error, you have entered neither C or F")
