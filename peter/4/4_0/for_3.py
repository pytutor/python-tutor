# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:11:53 2013

@author: pboehling
"""

# Schleife - Vorzeitige Rueckkehr zum Anfang
import numpy as np
n = 10
n_end = 5 

for k in np.arange(n):
    print(['1a: k = ',str(k)])
    if k >= n_end:
        print ('Rueckkehr')
        break
    print(['1b: k = ',str(k)])
