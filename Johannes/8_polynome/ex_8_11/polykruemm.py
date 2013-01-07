# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:54:44 2012

@author: johannes
"""

from __future__ import division
import numpy as np

def polykruemm(p,x):
    y = np.polyval(p,x)
    dy = np.polyval(np.polyder(p),x)
    ddy = np.polyval(np.polyder(p,2),x)
    kappa = np.abs(ddy/(1+dy**2)**(3/2))
    mx = x - dy*(1+dy**2)/ddy
    my = y + (1+dy**2)/ddy
    return kappa,mx,my