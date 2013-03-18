# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:47:43 2013

@author: Peter
"""
import numpy as np
from gauss1d import gauss1d
###
x=np.arange(-5,0.1,5)
x0=np.array([-1,0,1])
sig=np.array([0.5,1.2,1.4])
g = gauss1d(x,x0,sig)
###



###
x=np.arange(-5,0.1,5)
g = gauss1d(x)
###
###
x=np.arange(-5,0.1,5)
g = gauss1d(x,[],[])
###
###
x =np.arange(-5,0.1,5)
x0 = np.array([-1 , 0 , 1])
sig = np.array([0.5 , 1.2])
g = gauss1d(x,x0,sig)
###

###
gauss1d([])
###

###
gauss1d()
###