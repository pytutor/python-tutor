import numpy as np
x = np.arange(1,6)
y = np.arange(2,7)

a = 2.5
b = 3.1

r1 = x + y
r2 = x * y
r3 = x / y
r4 = x ** y
r5 = x / a
r6 = a/ x
r7 = a / (x + b)
r8 = x ** (y + a)
r9 = (x+b) **y
print(r9)