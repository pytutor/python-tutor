# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:15:52 2013

@author: pboehling
"""

# Schleife - Durchlauf durch eine Matrix
import numpy as np

x = np.array([1,5,9, 3,4,7])
print(['x: ',str(x)])

p = 1 # Initialisierung
for k in np.arange(sum(np.shape(x))): #  1 bis Anzahl der Elemente
    v = x[k] # k: Index
    p = p * v
    print([
        ' Index: ', str(k), 
        ' Wert: ', str(v), 
        ' Produkt: ',str(p) 
        ])    
