
for i in range(6):
    for j in range(5, i, -1):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
for i in range(6):
    for j in range(i):
        print(" ", end="")
    for k in range(5, i, -1):
        print("*", end="")
    print()
