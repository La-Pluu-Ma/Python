
num = [12, 75, 150, 180, 145, 525, 50]

for item in num:
    if item % 5 == 0 and item <= 150:
        print(item)
    elif item > 500:
        break