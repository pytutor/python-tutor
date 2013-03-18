# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 21:30:17 2013

@author: Peter
"""

import ellipse 
import hyperbel

[phi,r] = ellipse.ellipse(150,3,4)

[phi,r] = ellipse.ellipse(150,5,4)

[phi,r] = hyperbel.hyperbel(150,5,4,1)

[phi,r] = hyperbel.hyperbel(150,5,4,6)

