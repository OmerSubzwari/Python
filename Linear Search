def lsearch(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i # Return the index where the target is found
    return -1 # If the val,ue is not found, return -1

# List:
list = [10,25,4,7,236,844,64,11,6,34,74,32,77,83]

# Starting/Exiting loop
user = str(input("Enter Y to start, N to exit: "))

if user.lower() == "n":
    print("Goodbye!")

print("")

while user.lower() == "y":  
    # Taking input for value to search:
    target = int(input("Please enter the value you want to find: "))

    position= lsearch(list,target)
             
    if position != -1:
        print("Element", target,"was found at index", position)
    else:
        print("Element", target,"was not found in the list.")

    user = str(input("Enter Y to continue, N to exit: "))

    if user.lower() == "n":
        print("Goodbye!")

    print("")
