# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:23:45 2012

@author: johannes
"""

import numpy as np

def polytang(p,x0):
    p_der = np.polyder(p);

    y0 = np.polyval(p,x0);
    y0_der = np.polyval(p_der,x0);

    return y0_der, y0-y0_der*x0