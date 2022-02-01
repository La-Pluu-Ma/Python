
tp = tuple(map(int, input("Enter tuple with space : ").split()))
print(f"You can slice between 1 and {len(tp)}.")
while True:
    start = int(input("Enter start = "))
    end = int(input("Enter end = "))
    if start > 0 and end <= len(tp) and end > 0:
        break
l = list(tp)
for i in range(start, end, 1):
    print(l[i], end=" ")
