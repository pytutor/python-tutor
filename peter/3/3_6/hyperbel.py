# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 21:27:31 2013

@author: Peter
"""
import numpy as np
def hyperbel(n_points,a,b,r_0):

    if(r_0 <= a):
        print('r_0 > a ist nicht erfuellt')
        return(0,0)
    
        
    e=np.sqrt(a**2+b**2);
    epsilon = e/a
    phi_min = - np.arccos(np.sqrt((1+b**2/r_0**2)/epsilon**2))
    phi_max = - phi_min
    phi = np.linspace(phi_min,phi_max,n_points)
    r = np.sqrt(b**2/(epsilon**2*np.cos(phi)**2-1))
    
    return(phi,r)