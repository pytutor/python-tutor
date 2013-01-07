# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 07:41:22 2012

@author: johannes
"""

import numpy as np
import pylab as plt

rad = 6
N = 120
x = np.linspace(-rad,rad,N/2)
y = np.sqrt(rad**2-x**2)
y = np.append(y,-y)
phi = np.linspace(0,2*np.pi,N)

fig = plt.figure()

plt.plot(np.append(x,x),y,'r*')
plt.axis('equal')
plt.polar(phi,rad*np.ones(N),'bo')

plt.show()