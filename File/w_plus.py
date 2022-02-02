
file = open("hello.txt", "w+")

file.read()
lines = input("Enter string : ")

file.write(lines + "\n")

file.close()