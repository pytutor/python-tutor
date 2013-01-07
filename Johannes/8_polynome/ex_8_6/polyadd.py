# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:47:22 2012

@author: johannes
"""

import numpy as np

def polyadd(p1,p2):
    s1 = np.size(p1)
    s2 = np.size(p2)
    length = max(s1,s2)
    p1 = np.insert(p1,np.zeros( length-s1 >= 0 and length-s1 or 0),0)
    p2 = np.insert(p2,np.zeros( length-s2 >= 0 and length-s2 or 0),0)
    return p1+p2