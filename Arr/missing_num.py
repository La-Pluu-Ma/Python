
from array import array
a = array('i', [10, 11, 12, 13, 14, 16, 18, 19, 20])
n = 10
for i in range(len(a)):
    if a[i] != n:
        print(f"Missing : {n}")
        n = n + 1
    n = n + 1
