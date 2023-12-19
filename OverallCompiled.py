import time

name = ['arafat', 'bandeshah', 'hashir', 'ieshan', 'imran', 'omer', 'rumaisa', 'saad', 'saarim', 'sakina', 'usman', 'zahra'] #Name array for searching
number = [5,11,12,22,23,25,26,34,64,72,74,90,100] #Number array for searching

name1 = ['bandeshah', 'hashir', 'arafat', 'ieshan', 'sakina', 'zahra', 'omer', 'rumaisa', 'saarim', 'imran', 'usman', 'saad'] # Unsorted Name Array for bubble sort 
number1 = [11,23,36,84,23,62,73,88,43,54,6,1,88,100,91] # Unsorted Number Array for bubble sort

name2 = ['bandeshah', 'hashir', 'arafat', 'ieshan', 'sakina', 'zahra', 'omer', 'rumaisa', 'saarim', 'imran', 'usman', 'saad'] # Unsorted Name array for insertion sort
number2 = [11,23,36,84,23,62,73,88,43,54,6,1,88,100,91] # Unsorted Number array for insertion sort

# Functions and procedures:

def linearsearch(arr,target): #Linear Search function
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binarysearch(arr,target): #Binary Search function
    ub = len(arr) - 1
    lb = 0
    while ub>=lb:
        mid = (ub+lb)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            ub = mid - 1
        else:
            lb = mid + 1
    return -1

def bubblesort(arr):
    swapped = True
    i = len(arr)
    while swapped:
        swapped = False
        n = 1
        while i > n:
            if arr[n-1] > arr[n]:
                arr[n-1],arr[n] = arr[n], arr[n-1]
                swapped = True
            n += 1

def insertionsort(arr):
    i = 1
    while i <= (len(arr)-1):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_element
        i += 1

def factorial(n):
    # Base Case: Recursion stops and value returns
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive Case: Recursion continues until base case occurs
        return n * factorial(n-1)
    
# Searching methods:

print("--------Linear Search---------") # Gap

namesearch = str(input("Enter the name you want to search for: ")) # Linear Search for name array
found = linearsearch(name1,namesearch.lower())
if found != -1:
    print(f"Name {namesearch} was found at index {found}.")
else:
    print(f"Name {namesearch} was not found in the list.")


numsearch = int(input("Enter the number you want to search for: ")) # Linear Search for numbers array
found = linearsearch(number1,numsearch)
if found != -1:
    print(f"Number {numsearch} was found at index {found}.")
else:
    print(f"Number {numsearch} was not found in the list.")

time.sleep(1)

print("--------Binary Search---------") # Gap

namesearch = str(input("Enter the name you want to search for: ")) # Binary Search for name array
found = binarysearch(name,namesearch.lower())
if found != -1:
    print(f"Name {namesearch} was found at index {found}.")
else:
    print(f"Name {namesearch} was not found in the list.")


numsearch = int(input("Enter the number you want to search for: ")) # Binary Search for numbers array
found = binarysearch(number,numsearch)
if found != -1:
    print(f"Number {numsearch} was found at index {found}.")
else:
    print(f"Number {numsearch} was not found in the list.")

time.sleep(1)

# Sorting methods:

print("--------Bubble Sort---------") # Gap

print("Unsorted Name Array:") # Bubble sort for names1 array
for x in range(len(name1)):
    print(name1[x])

print("")

print("Sorted Name Array:")
bubblesort(name1)
for x in range(len(name1)):
    print(name1[x])

print("----------------------------")

print("Unsorted Number Array:") # Bubble sort for number1 array
for x in range(len(number1)):
    print(number1[x])

print("")

print("Sorted Number Array:")
bubblesort(number1)
for x in range(len(number1)):
    print(number1[x])

print("")

time.sleep(1)

print("--------Insertion Sort---------") # Gap

print(f"Unsorted name list: {name2}") # Insertion sort for name2 array
insertionsort(name2)
print(f"Sorted name list: {name2}")

print("----------------------------")

print(f"Unsorted number list: {number2}") # Insertion sort for number2 array
insertionsort(number2)
print(f"Sorted number list: {number2}")

print("")
# Recursive Function:

time.sleep(1)

print("--------Recursive Function---------")

result = int(input("Enter your number: "))
print(factorial(result))



