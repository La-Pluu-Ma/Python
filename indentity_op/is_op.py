a = input("Enter an integer : ")

b = a
print(id(a))
print(id(b))
if a is b:
    print("True")
elif a is not b:
    print("False")