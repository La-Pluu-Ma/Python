
def square(x):
    """This function is square."""
    y = x ** 2
    return y

num = int(input("Enter the number : "))
print(f"The square of {num} is {square(num)}.")
print(f"The square of {num + 1} is {square(num + 1)}.")
print(square.__doc__)