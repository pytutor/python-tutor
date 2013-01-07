# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:02:47 2012

@author: johannes
"""

from ex_8_9 import polykruemm
import numpy as np

p = [-0.2,1.2,-1.35] 
x = np.array([1,2,3])
kappa,mx,my = polykruemm(p,x)