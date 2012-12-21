## boolean indexing
from numpy import *

a = arange(12).reshape(3,4)
b = a > 4
print(a[b])
print(a[~b])

a[b] = 0

b1 = array([False,True,True])
b2 = array([True,False,True,False])

print(a[b1,:])
print(a[:,b2])
a[b1,b2]