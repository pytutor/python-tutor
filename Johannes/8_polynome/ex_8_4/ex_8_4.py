# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:52:27 2012

@author: johannes
"""

import numpy as np
from polyadd import polyadd

def polyintersec(p1,p2):
    r = np.roots(polyadd(p1,-p2))
    x = r[np.isreal(r)]
    y = np.polyval(p1,x)
    return x,y
