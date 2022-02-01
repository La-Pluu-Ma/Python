
f = 0
s = 1
t = f + s
print("Fibonacci sequence:")
print(f, end="  ")
print(s, end="  ")
for i in range(8):
    print(t, end="  ")
    f = s
    s = t
    t = f + s
