# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:54:57 2012

@author: johannes
"""

from polyintersec import polyintersec
import numpy as np
from ex_8_6 import poly_area

p1 = np.array([0.1,-0.7,1.4,-0.8])
p2 = np.array([-0.2,1.2,-1.35])
x,y = polyintersec(p1,p2)
A = poly_area(x[1],x[2],p1,p2)