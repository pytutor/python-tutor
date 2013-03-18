# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:00:52 2013

@author: pboehling
"""

import numpy as np

m = 5
n = 4
x = np.arange(m)

# Initialisierung der Summe
s = np.zeros((1,m)) #  Nullen; 1-Zeile; m-Spalten
for k in np.arange(n):
    s = s + x*k
    print(['s = ',str(s)])


print(' ')

# Initialisierung des Produkts
p = np.ones((1,m)) # Einsen; 1-Zeile; m-Spalten
for k in np.arange(n):
    p = p +  x*k
    print(['p = ',str(p)])
