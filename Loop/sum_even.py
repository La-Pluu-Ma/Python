
positive = True
sum = 0
while(positive is True):
    n = int(input("Enter positive integer :"))
    if(n > 0):
        sum = sum + n
        positive = True
    else:
        positive = False

print(f"Sum = {sum}")
