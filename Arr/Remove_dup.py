
from array import array
a = array('i', [1, 3, 5, 1, 3, 7, 9])
s = set(a)
a = array('i', list(s))
print(a)
