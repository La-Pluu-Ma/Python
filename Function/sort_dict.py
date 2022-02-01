
z = {}
key = "p1 p2 p3 p4".split()
values = "100 122 342 142".split()
for i in range(len(key)):
    z.update({key[i]:values[i]})
print(z)