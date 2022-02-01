
tu = tuple(input("Enter tuples separated by a space : ").split())
l = list(tu)
d = []
for item in tu:
    if l.count(item) > 1 and item not in d:
        d.append(item)

tu = tuple(d)
print(tu)
