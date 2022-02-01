
while True:
    tu = tuple(input("Enter at least 4 elements tuple : ").split())
    if len(tu) >= 4:
        break
print(tu)
print(tu[3])
print(tu[-4])
