
string = input("Enter strings : ").split()
count = 0
for item in string:
    if len(item) >= 2 and item[0] == item[-1]:
        count += 1

print(count)
