# Python Skript: 1_4
# Einfaches Plotprogramm
# Name: Peter Boehling   
# Datum: 23.01.13
import numpy as np
import matplotlib.pyplot as plt

x_start = -4
x_end   = 4
x_delta = 0.1

x_1 = np.arange(x_start,x_end)
y_1 = x_1 * np.abs(x_1)

x_2 = np.arange(x_start,x_end,x_delta)
y_2 = x_2**2+1/(x_2**2+75)

plt.figure()
plt.plot(x_1,y_1,'ro-',x_2,y_2,'bo-')
plt.show()