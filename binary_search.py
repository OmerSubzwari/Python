def search(arr, found):

    ub = len(arr) - 1
    lb = 0

    while ub >= lb:
        mid = (ub + lb) // 2

        if arr[mid] == found:
            return mid

        elif found < arr[mid]:
            ub = mid - 1
        else:
            lb = mid + 1
    return -1

name = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "h"]
chosen = str(input("Please enter your character: \n"))
result = search(name, chosen)

if result != -1:
    print(f"Your character {chosen}, was found at index {result}.")
else:
    print(f"Your character {chosen}, was not found in the list.")
