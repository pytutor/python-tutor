# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:58:07 2012

@author: johannes
"""

import numpy as np
def ellipso(a,b):
    t = np.linspace(0,2*np.pi,100)
    x = a*np.cos(t)
    y = b*np.sin(t)
    return x,y
    
    
import matplotlib.pyplot as plt
plt.figure()
x,y=ellipso(2,1)
plt.plot(x,y)
plt.show()