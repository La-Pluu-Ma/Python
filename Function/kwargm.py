
def printme(name, age, **kwargs):
    print(f"My name is {name} and I am {age} years old.")
    print(kwargs)

printme("Bob", 5, gender = "Male", address = None)
