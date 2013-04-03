# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:38:12 2012

@author: johannes
"""

import numpy as np

A = np.array([ [6,   1, -3],\
		[8,   8,  0],\
		[-2,   0,  1 ]])

b = np.array([  3,3,11 ])
x = np.linalg.solve(A,b)
print('x = ' + str(x))