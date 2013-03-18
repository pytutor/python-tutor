# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:19:13 2013

@author: Peter
"""

import numpy as np
def schwebung(t,nu1=None,nu2=None,A=None):
    
    if t == None:
        print('Time vector is undefined')
        return(0,0)
    if nu1 == None:
        nu1 = 5.0
    if nu2 == None:
        nu2 = 4.5
    if A == None:
        A  = 1.0
    
    x = A*(np.sin(2*np.pi*nu1*t) + np.cos(2*np.pi*nu2*t))
    y = A*(np.sin(2*np.pi*nu1*t) - np.cos(2*np.pi*nu2*t))
    return(x,y)