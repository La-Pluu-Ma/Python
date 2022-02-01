
tu = tuple(input("Enter a tuple : ").split())
item = input("Enter the wanted item : ")

li = list(tu)
for i in range(len(li)):
    if item == li[i]:
        print(f"The index of {item} is {i}.")