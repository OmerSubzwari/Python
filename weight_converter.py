x = 1
while x <=5:
    weight = float(input("Input your Weight: "))
    if weight > 1000:
        print ("Sorry, your weight exceeds the numerical limit of our system")
        exit()
    else:
        type = input("Choose (K)g or (L)bs: ")
        if type.upper() == "K":
            convert = float(weight) * 2.205
            print ("Your weight in Lbs is: " + str(convert))
        elif type.upper() == "L":
            convert = float(weight) / 2.205
            print ("Your weight in Kg is: " + str(convert))
        elif type.upper() != "K" or type.upper() != "L":
            print ("Error, you have entered neither K or L.")
    x = x + 1





