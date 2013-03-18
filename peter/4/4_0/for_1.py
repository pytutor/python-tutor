# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 13:56:50 2013

@author: pboehling
"""
import numpy as np
n = 5

for k in np.arange(n):
    print(['1: k = ',str(k)])


print(' ') # Leerzeile

x = np.arange(n) # Zeilenvektor
for k in x:
    print('2: k = ',str(k))
