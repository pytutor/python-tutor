# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:44:34 2013

@author: Peter
"""
import numpy as np
import matplotlib.pyplot as plt
from logspirale import logspirale
t_min = 0 
t_max = 1.7 
nodes = 400 
t = np.linspace(t_min, t_max, nodes) 

[x,y] = logspirale(t)
tit = 'Logarithmische Spirale' 

plt.figure()
plt.plot(x,y)

plt.title(tit)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
    