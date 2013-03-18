# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:28:04 2013

@author: Peter
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as sp
N = 6
x = np.linspace(-np.pi,np.pi,100)

y = np.zeros((np.shape(x)))

plt.figure()
plt.plot(x,y)


for n in np.arange(0,7):
    y = y + (-1)**n * x**(2*n+1) / sp.factorial(2*n+1)
    plt.plot(x,y)



plt.plot(x,np.sin(x),'r--')
