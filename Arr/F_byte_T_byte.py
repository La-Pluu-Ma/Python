
from array import array
a = array('i', [7, 8, 9, 10])
b = a.tobytes()
print(a)
print(b)
c = array('i')
c.frombytes(b)
print(c)
