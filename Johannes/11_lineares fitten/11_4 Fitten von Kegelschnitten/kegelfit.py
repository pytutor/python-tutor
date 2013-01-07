# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 14:46:47 2012

@author: johannes
"""

import numpy as np
import pylab as plt

#def kegelfit(xd,yd):
data = np.loadtxt('data.dat')
xd = data[:,0]
yd = data[:,1]



#    A = np.array([[1,2],[1,4]])
#    c = np.array([1,3])
#    x = np.linalg.solve(A,c)