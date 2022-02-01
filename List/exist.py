
tu = tuple(input("Enter tuples by space : ").split())
test = list(tu)
count = 0

ele = input("Enter the desired word : ")
for item in test:
    if ele == item:
        print("It exists in the tuple!")
        count+=1

if count == 0:
    print("It does not exit!")
