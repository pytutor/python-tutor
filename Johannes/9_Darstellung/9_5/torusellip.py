# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 08:01:57 2012

@author: johannes
"""

import numpy as np
import pylab as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

N = 50
a = 1
b = 1

R = 2 * np.ones(N)
theta = np.linspace(0,2*np.pi,N)
phi = np.linspace(0,2*np.pi,N)

theta,phi = np.meshgrid(theta,phi)
x = (R+ a*np.cos(theta))*np.cos(phi)
y = (R+ a*np.cos(theta))*np.sin(phi)
z = b*np.sin(theta)
fig = plt.figure() # erzeugen er figure
ax = fig.gca(projection='3d') # "get current axes", erzeugt die Achsen für den 3D-Plot
col = (R+np.sqrt(a**2+b**2)*np.cos(2*theta) * np.cos(2*phi))
col = col/col.max()
# Erzeugen des 3D-Plots, wobei col die (normierten) Funktionswerte für die
# Farbdarstellung enthält, die letzten beiden Parameter definieren die Schrittweite im Plot
surf = ax.plot_surface(x, y, z,facecolors=cm.jet(col),rstride=1, cstride=1)
plt.show() # anzeigen des Plots
