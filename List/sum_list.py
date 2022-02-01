
lis = input("Enter integers seperating by space : ").split()

for i in range(len(lis)):
    lis[i] = int(lis[i])

print(sum(lis))
