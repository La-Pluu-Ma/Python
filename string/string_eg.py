
string = "Hello! I am Orion!"

if "Hello" in string:
    print(f"Found!")

if "HBH" not in string:
    print(f"Not found!")

print(string[:5])
print(string[5:])
print(string[2:5])
print(string[-5:-2])
print(string[::-1])
print(string.strip("!"))
string2 = string.replace("i", "A")
print(string2)

print(string.split())

name = 'Alice'
age = 21
temp = "{} is {} years old.".format(name, age)
print(temp)

test = "File file?!!    FIle fILe ff@"

print(test.find("file"))
print(string.capitalize())
print(string.casefold())
print(test.count("f"))
print(test)
y = "Hello \t hi"
print(y.expandtabs(15))
print(test.casefold())
print(test.encode("ascii", "ignore"))
A = 'EndOfTheLine11'
print(A.isalnum())
print(test.center(40), "Is")
print('#'.join(test))
x = test.rjust(40)
print(x)
print(test.split())
print(test.swapcase())
print(test.title())
