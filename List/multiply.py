
a = input("Enter the integer for the list seperating with a space: ").split()
res = 1
for i in range(len(a)):
    a[i] = int(a[i])

for j in range(len(a)):
    res = res * a[j]

print(res)
