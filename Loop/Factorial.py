
while True:
    n = int(input("Enter positive integer :"))
    if n >= 0:
        break

fact = 1
for i in range(1, n + 1, 1):
    fact = fact * i
print(f"Factorial of {n}! is {fact}.")