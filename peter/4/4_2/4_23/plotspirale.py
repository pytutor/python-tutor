# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:28:00 2013

@author: Peter
"""
import numpy as np
import matplotlib.pyplot as plt
from spirale import spirale

t_min = 0 
t_max = 1.7 
nodes = 400 
t = np.linspace(t_min, t_max, nodes) 

[x,y] = spirale(t)
tit = 'Spirale' 

plt.figure()
plt.plot(x,y)

plt.title(tit)
plt.xlabel('x')
plt.ylabel('y')
plt.show()