# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:26:19 2012

@author: johannes
"""

import numpy as np
import pylab as plt

N = 100
n = 34
x = np.linspace(0,np.pi,N)
y = np.sin(x)
a = np.linspace(0,np.pi,n)
a = np.sin(a)

line, = plt.plot(0,0)
plt.xlim((min(x),max(x)))
plt.ylim((0,1))

for an in a:
    line.set_xdata(x)
    line.set_ydata(an*y)
    plt.draw()
    plt.pause(0.1)