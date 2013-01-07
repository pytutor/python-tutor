# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 16:49:19 2012

@author: johannes
"""

import numpy as np
from scipy.integrate import quad
def polylength(x1,x2,p):
    fun = lambda x: np.sqrt( 1 + (np.polyval(np.polyder(p),x))**2 ) 
    A = np.abs(quad(fun,x1,x2));
    return A[0]
