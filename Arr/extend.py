
from array import array
a = array('i', [1, 3, 5, 3, 7, 9, 3])
a.extend(a)
print(a)