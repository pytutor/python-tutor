# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 16:43:52 2012

@author: johannes
"""

import numpy as np
from scipy.linalg import solve

m = 2 # Masse 
kappa = 0.0 # Reibungskoeffizient

# Geschwindigkeit vd zur Zeit td
td  = np.array([0,2,9,10])
vd  = np.array([0,10,10,0])
# Ableitung der Geschwindigkeit vdp zur Zeit tdp
tdp = np.array([0,10])
vdp = np.array([0,0])

# Gleichungssystem fuer Polynomfit
V = [\
    [td**5,td**4,td**3,td**2,td,np.ones(td.shape)] , \
    [5*tdp**4,4*tdp**3,3*tdp**2,2*tdp,np.ones(tdp.shape),np.zeros(tdp.shape)] \
    ]
b = [vd,vdp]

# Polynom fuer Geschwindigkeit v
v_p = solve(V,b)