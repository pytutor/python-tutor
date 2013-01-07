# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:22:18 2012

@author: johannes
"""

import numpy as np

def polyextreme(p):

  dp = np.polyder(p);  
  ddp = np.polyder(dp);
  dp_roots = np.roots(dp);

  min_max = np.polyval(ddp, dp_roots);

  xmax = dp_roots[min_max < 0];
  ymax = np.polyval(p,xmax);
  
  xmin = dp_roots[min_max > 0];
  ymin = np.polyval(p,xmin);

  xinfl = np.roots(ddp);
  yinfl = np.polyval(p,xinfl);
  
  return xmax,ymax,xmin,ymin,xinfl,yinfl