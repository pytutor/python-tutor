# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:15:52 2013

@author: Peter
"""

import numpy as np
import matplotlib.pyplot as plt
from schwebung import schwebung

t_min=0
t_max=4
nodes=400

t = np.linspace(t_min, t_max, nodes)
[x,y] = schwebung(t)

plt.figure()
plt.plot(t,x,t,y,'r')
plt.title('Schwebung')
plt.xlabel('t')
plt.ylabel('Amplitude')

plt.figure()
plt.plot(x,y)

plt.title('Lissajous-Figur')
plt.xlabel('x')
plt.ylabel('y')
plt.show()