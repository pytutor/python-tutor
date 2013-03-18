# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:00:36 2013

@author: Peter
"""
import numpy as np
def logspirale(t,nu=None,A=None,gam=None):
    if t == None:
        print('Time vector is undefined')
        return(0,0)
    if nu == None:
        nu = 3.3
    if A == None:
        A = 1.1
    if gam == None:
        gam = 0.9
    
    x = A*np.log(1+gam*t)*np.cos(2*np.pi*nu*t)
    y = A*np.log(1+gam*t)*np.sin(2*np.pi*nu*t)
    return(x,y)
