
num = int(input("Enter a number : "))
r = 0
while num != 0:
    r = (r * 10) + (num % 10)
    num = num // 10

print(r)
