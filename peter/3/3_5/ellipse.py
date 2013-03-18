# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 21:22:16 2013

@author: Peter
"""
import numpy as np

def ellipse(n_points,a,b):
    


    if a < b:
        print('a >= b ist nicht erfuellt')
        return(0,0)
    
    
    
    
    e = np.sqrt(a**2-b**2)
    epsilon = e/a
    phi_min = 0
    phi_max = 2*np.pi
    phi = np.linspace(phi_min,phi_max,n_points)
    r = np.sqrt(b**2/(1-epsilon**2*np.cos(phi)**2))
    
    return(phi, r)