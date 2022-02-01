
dic = {}
for i in range(6):
    name = input("Enter name : ")
    mark = int(input("Enter mark : "))
    dic.setdefault(name,mark)
a = sorted(dic.values())
print(a[0:5])