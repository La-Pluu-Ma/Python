
n = int(input("Enter n : "))
k = 1
for i in range(1, n + 1):
    for j in range(i):
        print(k, end="  ")
        k = k + 1
    print()