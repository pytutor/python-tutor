# -*- coding: utf-8 -*-
"""
Created on Wed Mar 06 08:07:42 2013

@author: Peter
"""

import numpy as np
from numpy import random
def array_randsym(m = None):

    if m ==  None:
        m=9
    
    r = random.rand(m,m)
    oben = np.triu(r)
    unten = np.transpose(np.triu(r,1))
    A= oben + unten
    return(A)
    
