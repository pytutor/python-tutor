# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 18:35:43 2012

@author: johannes
"""

import numpy as np
import pylab as plt


def calculateParity(Z,N):
    
    return S
    
    
data = np.loadtxt('kern.txt')
M = data[:,0]
Z = data[:,1]
N = data[:,2]
E = -1*data[:,3]

S = calculateParity(Z,N)

Massencheck = all((N+Z)==M)
Energycheck = all(E>0)