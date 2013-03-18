# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 20:07:24 2013

@author: Peter
"""

import numpy as np 

def array_numberst(m = None,n = None):

    if m == None:
        m = 4
    if n == None:
        n = 5
    
    v = np.zeros((1,m*n))
    v[0,np.arange(0,m*n,2)] = np.arange(2,m*n+1,2)
    A= np.reshape(v,(n,m))
    return(A) 


