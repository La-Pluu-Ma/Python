
dic = {}
sum = 0
n = int(input("Enter how many numbers do you want to add : "))
for i in range(n):
    dic.setdefault(f'{i + 1} term number', int(input(f"Enter {i + 1} term number : ")))
    sum = sum + dic[f'{i + 1} term number']

print(dic)
print(sum)