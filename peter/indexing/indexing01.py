## indexing lessons

from numpy import *

a = arange(12)**2
i = array( [ 1,1,3,8,5 ] )
print(a[i])
j = array( [ [ 3, 4], [ 9, 7 ] ] )
print(a[j])

a = arange(12).reshape(3,4)
i = array( [ [0,1],[1,2] ] )
j = array( [ [2,1],[3,3] ] )
print(a[:,j])
print(a[i,2])
print(a[i,j])