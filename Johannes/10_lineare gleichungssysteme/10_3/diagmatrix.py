# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 10:59:57 2012

@author: johannes
"""

import numpy as np

try:
    n = input('Dimension: ')
except:
    n = 5


dim = 2*n
M = np.eye(dim)+ 0.5*(np.eye(dim,dim,1)+ np.eye(dim,dim,-1))

v = np.zeros(dim)
v[1::2] = np.arange(1,n+1)

y = np.linalg.solve(M,v)
check = np.dot(M,y)-v

print('check' + str( check==0 ))

error_limit = 1E-8

if(all(abs(check) < error_limit)):
    print 'Check successful'
else:
    print 'Check not successful'