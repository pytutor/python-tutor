# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 20:29:52 2013

@author: Peter
"""

import numpy as np
def array_setnan(m= None ,n = None):

    if m == None:
        m = 5
    if n == None:
        n = 9
    
    
    A=np.ones((m,n))
    A[[-1,-1,0,0,],[0,-1,0,-1]]=np.NaN
    A[1:-1,1:-1]=np.NaN
    return(A)
    