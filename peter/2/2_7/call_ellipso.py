# -*- coding: utf-8 -*-
"""
Created on Thu Feb 07 18:37:11 2013

@author: Peter
ruft die function ellipso auf
"""

from ellipso import *
import matplotlib.pyplot as plt
a=5
b=3
[x,y]=ellipso(a,b)
plt.plot(x,y,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.show()
