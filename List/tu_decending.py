
mt = []
lo = []
n = int(input("Enter the amount of tuple : "))
for i in range(n):
    temp = tuple(map(int, input("Enter a tuple : ").split()))
    mt.append(temp)

print(mt)
t = mt[0][-1]
for i in range(n):
    for j in range(n):
        if mt[j][-1] < mt[i][-1]:
            t = mt[i]
            mt[i] = mt[j]
            mt[j] = t
lo = tuple(mt)
print(lo)
