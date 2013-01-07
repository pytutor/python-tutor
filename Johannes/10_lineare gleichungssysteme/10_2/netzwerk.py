# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:38:12 2012

@author: johannes
"""

import numpy as np

A = np.array([ [1, - 1,  1],\
      [0,  10, 25],\
      [20,  10,  0 ]])
U = np.array([[ 0,   0,   0],\
    [60, 100, 160],\
	[80,  90,  90]])

#1.
b = U[:,0]
I1 = np.linalg.solve(A,b)

#2.
b = U[:,1]
I2 = np.linalg.solve(A,b)
  
#3.
B = U;
I = np.linalg.solve(A,B)