
tu = tuple(input("Enter at least 6 tuples separated by a space : ").split())
l = list(tu)
m = []
for i in range(len(l)):
    if i != 0 and i != 4 and i != 5:
        m.append(l[i])
tu = tuple(m)
print(tu)
