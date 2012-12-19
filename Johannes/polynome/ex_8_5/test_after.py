# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:30:45 2012

@author: johannes
"""
from __future__ import division
import numpy as np
from ex_8_5 import polyextreme
import pylab as plt

p = np.array([1/20,3/20,-11/20,-27/20,1/2,16/5])

xmax,ymax,xmin,ymin,xinfl,yinfl = polyextreme(p)

x = np.arange(-4,3.1,0.1)
plt.plot(x,np.polyval(p,x),xmax,ymax,'ro',xmin,ymin,'md',xinfl,yinfl,'ks')
plt.title('Testpolynom')
plt.legend(['P','max','min','infl'])
plt.show()