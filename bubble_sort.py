def bubble_sort(name):
    flag = False
    i = len(name) - 1
    while i > 0:
        for j in range(i):
            if name[j] > name[j + 1]:
                temp = name[j]
                name[j] = name[j + 1]
                name[j + 1] = temp
                flag = True
        if not flag:
            break
        flag = False
        i -= 1

name = ["Omer", "Usman", "Bandeshah", "Sakina", "Saad", "Arafat", "Zahra"]

print("Unsorted Names: ")
for x in range(7):
    print(name[x])

print(" ")

bubble_sort(name)
print("Sorted Names: ")
for x in range(7):
    print(name[x])
    
