s = set(map(int, input("Enter set : ").split()))

n = int(input("Enter remove item : "))

if n in s:
    s.remove(n)
    print(s)
else:
    print(f"Not present!\n{s}")