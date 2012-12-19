# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:18:09 2012

@author: johannes
"""

from ex_8_4 import polyintersec
import numpy as np

p1 = np.array([1,2,3])
p2 = np.array([4,2,7,1])
x,y = polyintersec(p1,p2)