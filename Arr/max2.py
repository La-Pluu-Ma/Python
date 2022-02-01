
from array import array
a = array('i', [1, 2, 3, 4, 7, 0, 8, 4])
print(f"Oringinal = {a}")
m1 = max(a)
a.remove(m1)
m2 = max(a)
print(f"({m1}, {m2})")
