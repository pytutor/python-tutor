# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:15:01 2013

@author: Peter
"""

import numpy as np

def randmeanfor(R):

    mean_p = 0
    count_p = 0
    mean_n = 0 
    count_n = 0
    shape = np.shape(R)
    R = np.reshape(R, np.size(R))
    
    for k in np.arange(np.size(R)):
        if     R[k] > 0:
            mean_p = mean_p + R[k] 
            count_p = count_p + 1
        elif R[k] < 0:
            mean_n = mean_n + R[k] 
            count_n = count_n + 1
    
    
    mean_p = mean_p / count_p
    mean_n = mean_n / count_n
    
    for k in np.arange(size(R)):
        if     R[k] > 0:
            R[k] = mean_p
        elif R[k] < 0:
            R[k] = mean_n
    R = np.reshape(R, shape)    

    return(R)