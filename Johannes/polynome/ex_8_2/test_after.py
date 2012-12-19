# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:20:05 2012

@author: johannes
"""
from ex_8_2 import polyadd
p1 = np.array([2, 5, 6])
p2 = np.array([2 ,5, 1, 7, 9])

pout_1 = polyadd(p1,p2) 
pout_2 = polyadd(p2,p1) 
pout_3 = polyadd(p1,p1) 