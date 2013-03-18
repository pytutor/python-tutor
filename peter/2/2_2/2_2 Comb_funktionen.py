# Python-Skript: Komb Funktionen
# Plotten von Funktionen
# Name: Peter Boehling
# Datum: 13.01.2012
# Original Winfried Kernbichler 2006 Matlab

import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

x_a = -2*pi
x_e = 2*pi
x_n = 180

x = np.linspace(x_a,x_e,x_n)

f1= np.sin(x) * x / (2*pi)
f2= np.sin(x)**2 * x**2 / (2*pi)**2
f3= np.sin(x)**3 * x**3 / (2*pi)**3

plt.figure()
plt.plot(x,f1,'r',x,f2,'b',x,f3,'g')
plt.xlim(x_a,x_e)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(('f1(x)','f2(x)','f3(x)'),loc = 8)
plt.show()