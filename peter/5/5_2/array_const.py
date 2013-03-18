# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 19:59:32 2013

@author: Peter
"""

import numpy as np

def array_const(m = None,n = None,v = None):

    if m == None:
        m = 10
    if n == None:
        n = 13
    if v == None:
        v = 15
    
    
    r = np.ones((m,n))*v
    return(r)


