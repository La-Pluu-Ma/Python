
def check(num):
    """This function is for checking even or odd for the given number."""
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input("Enter the number : "))
if num == 0:
    print(f"{num} is neither.")
elif check(num) == True:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")