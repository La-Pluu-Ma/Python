
n = int(input("Enter the integer (1 to 5) : "))
if(1<=n<=5):
    for i in range(1, 11, 1):
        for j in range(1, n + 1, 1):
            print(f"{j} x {i} = {j * i}\t", end="")
        print()
else:
    print(f"Please Enter again!")