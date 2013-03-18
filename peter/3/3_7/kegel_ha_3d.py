# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 20:46:57 2013

@author: Peter
"""
import numpy as np
import pylab as p2
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import mpl_toolkits.mplot3d.axes3d as p3
n_points = 51  
a = 3  
b = 2  
p = 0.2 
delta = 2 

x = np.linspace(-a-delta,a+delta,n_points) 
y = np.linspace(-b-delta,b+delta,n_points) 

[xx,yy] = np.meshgrid(x,y) 

zz_zero = np.zeros((np.shape(xx))) 
zz_e = (xx/a)**2 + (yy/b)**2 -1 
zz_h = (xx/a)**2 - (yy/b)**2 -1 
zz_p = yy - p*xx**2 

col_grey    = [0.2,0.2,0.2] 
alpha_kegel = 0.9 
alpha_zero  = 0.8 

# Studenten muessen es nicht mit einer for-Schleife machen

for k in np.arange(1,4):
    
    if k ==  1:
        zz = zz_e 
    if k == 2:
        zz = zz_h 
    if k == 3:
        zz = zz_p 
    
    
    fig=p2.figure()
    ax = p3.Axes3D(fig)
    ax.plot_surface(xx,yy,zz, rstride=1, cstride=1, cmap=cm.Set1,
        linewidth=0, antialiased=False)

    ax.plot_wireframe(xx,yy,zz_zero, color = col_grey)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


p2.show()