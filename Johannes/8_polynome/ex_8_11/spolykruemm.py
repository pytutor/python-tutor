# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:40:48 2012

@author: johannes
"""

import numpy as np
from polyextreme import *
from kreis import *
from polykruemm import *
import pylab as plt

p = [-0.25,1.2,-1.4]
N = 200
w = np.linspace(-2,7,N)
phi = np.linspace(0,2*np.pi,N)
plt.figure()
plt.plot(w,np.polyval(p,w))
x_max = polyextreme(p)[0]
kappa,mx,my = polykruemm(p,x_max)
r = 1/kappa
x_circ,y_circ = kreis(r,mx,my,phi)
plt.plot(x_circ,y_circ)
plt.plot(mx,my,'rx')
x_rad,y_rad = kreis(r,mx,my,5*np.pi/4)
plt.plot([mx,x_rad],[my,y_rad],'k')
plt.axis('equal')
plt.title('Darstellung eines Schmiegekreises')
plt.xlabel('x')
plt.ylabel('y')
plt.show()