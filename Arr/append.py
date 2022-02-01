
from array import array
a = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print(f"Oringinal : {a}")
n = int(input("Enter append element : "))
a.append(n)
print(f"New : {a}")