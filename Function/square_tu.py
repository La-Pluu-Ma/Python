
def square(num):
    return num ** 2

li = (1, 2, 3, 4, 5)
print(li)
li = list(map(square, li))
print(li)