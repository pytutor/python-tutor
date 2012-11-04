# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:28:05 2012

@author: johannes
"""
import numpy as np
import matplotlib.pyplot as plt

def sgauss(x,x_0,s):    
    return 1/(s*np.sqrt(2*np.pi))*np.exp(-(x-x_0)**2/(2*s**2))
    
def smaxwell(v,m,T):
    return 4*np.pi * (m/(2*np.pi*T))**(3.0/2) * v**2 * np.exp(-m*v**2/(2*T))
    
def secansh(x,x_0,s):
    return 1/(np.pi*s*np.cosh(-(x-x_0)/s))
    
x_a=0
x_e=30
x_n=300
x = np.linspace(x_a,x_e,300)
plt.figure()
plt.plot(x,sgauss(x,10,5),x,secansh(x,10,5))
plt.show()