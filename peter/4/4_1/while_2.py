# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:45:01 2013

@author: pboehling
"""

# Bedingte Schleife
# Gefahr: unendliche Schleife

n = 10
k = 0

while k <= n:  #solange Bedingung wahr ist
    print(['1: k = ',str(k),' n = ',str(n)])
    k = k + 1
    n = n - 1

