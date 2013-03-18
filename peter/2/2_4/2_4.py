# Matlab-Skript: pskript
# Einfache mathematische Funktionen
# Name: Peter Boehling
# nach dem Matalabskript von Winfried Kernbichler
import numpy as np
import matplotlib.pyplot as plt

from sgauss import *
from secansh import *

x_0 = -1
s   = 0.1
x_a = x_0 - 5 * s
x_e = x_0 + 5 * s
x_n = 300

x = np.linspace(x_a,x_e,x_n)
g = sgauss(x,x_0,s)
h = secansh(x,x_0,s)

plt.figure()
plt.plot(x,g,'r',x,h,'b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend({'Gauss','Sech'},loc = 2)
plt.show()