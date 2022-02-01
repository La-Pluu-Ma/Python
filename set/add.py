s = {10, 20, 30, 40, 50}

n = list(map(int, input("Enter what you want to add : ").split()))
s.update(n)
print(s)
