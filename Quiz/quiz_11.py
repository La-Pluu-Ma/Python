
start = int(input("start = "))
end = int(input("end = "))

for i in range(start, end + 1):
    count = 0
    if i != 0 and i != 1:
        for j in range(2, (i//2) + 1):
            if i % j == 0:
                count = count + 1
        if count == 0:
            print(i)
