
l = [1, 2, 3, 4, 5]
n = int(input("Enter n : "))
for i in range(n):
    a = l[0]
    for j in range(len(l)):
        if j == 0:
            l[j] = l[len(l) - 1]
        else:
            temp = l[j + 1]
            l[j + 1] = l[j]
