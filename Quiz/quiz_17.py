
n = int(input("n = "))
series = 0
sum = 0
for i in range(1, n + 1):
    series = (series * 10) + 2
    sum = sum + series
print(sum)
