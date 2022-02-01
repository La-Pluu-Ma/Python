
dict = {}
n = int(input("Enter the number of the element : "))
for i in range(n):
    key = input("Enter the key : ")
    value = input("Enter the value : ")
    dict.update({key:value})
print(dict)

