# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:12:56 2013

@author: Peter
"""

import numpy as np

def randmeanlog(R):

    L_p = R>0
    L_m = R<0
    R[L_p]= np.mean(R(L_p))
    R[L_m]= np.mean(R(L_m))
    
    return(R)