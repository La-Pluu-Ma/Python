
file = open("hello.txt", "a")

text = input("Enter string : ")
file.write(text + "\n")

file.close()