
test = tuple(input("Enter a tuple : ").split())

print(f"Original = {test}")
rever = list(test)
rever.reverse()
test = tuple(rever)
print(f"Reverse = {test}")
