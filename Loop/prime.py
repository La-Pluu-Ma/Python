
while True:
    n = int(input("Enter a positive integer(greater than 1) : "))
    if(n > 1):
        break

temp = int(n / 2)
count = 0
for i in range(2, temp, 1):
    if n % i == 0:
        print(f"{n} is not a prime number.")
        count += 1
if count == 0:
    print(f"{n} is a prime number!")