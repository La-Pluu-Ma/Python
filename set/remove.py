s = {10, 20, 30, 40, 50}
n = int(input("Enter remove item : "))

if n in s:
    s.remove(n)
    print(s)
else:
    print("Not present!")

