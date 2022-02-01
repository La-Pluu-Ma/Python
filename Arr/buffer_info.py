
from array import array
a = array('i', [10, 20, 30, 40, 50, 60])
b = a.buffer_info()
print(b)
c = b[1]
print(c * a.itemsize)