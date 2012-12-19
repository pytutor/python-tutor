# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:39:18 2012

@author: johannes
"""

import numpy as np
import polyadd as pa

def poly_area(x1,x2,p1,p2):
    p = pa.polyadd(p1,-p2)
    i = np.polyint(p)
    print(i)
    return np.abs( np.polyval(i,x2) - np.polyval(i,x1))