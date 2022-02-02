
file = open("test.txt", "r")
test = file.read()
print(test)
test = file.readline()
print(test)
test = file.readlines()
print(test)

file.close()