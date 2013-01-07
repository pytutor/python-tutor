# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:18:35 2012

@author: johannes
"""

import numpy as np

def kreis(r,mx,my,phi):
    x = mx+r*np.cos(phi)
    y = my+r*np.sin(phi)
    return x,y
