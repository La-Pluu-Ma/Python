
from array import array
a = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
if len(a) !=len(set(a)):
    print(False)