# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:44:16 2013

@author: johannes
"""

import numpy as np

x = np.array([2, 1, 3, np.nan, 5, 2, 3, np.nan])
m = np.ma.masked_array(x, np.isnan(x))

av = np.mean(m)