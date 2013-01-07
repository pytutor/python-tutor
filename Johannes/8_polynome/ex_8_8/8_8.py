# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:48:35 2012

@author: johannes
"""

import numpy as np
from polyintersec import polyintersec
from poly_area import poly_area
from polylength import polylength
import pylab as plt

p1 = np.array([0.2,0.5,-2.4,-1.2])
p2 = np.array([-0.4,-1.5,0.7])

x,y = polyintersec(p1,p2)
x_y = zip(x,y)
x_y.sort()
x_y = np.array(x_y)
x_inter = x_y[:,0]
y_inter = x_y[:,1]

A = poly_area(x_inter[0],x_inter[1],p1,p2)
C = polylength(x_inter[0],x_inter[1],p1)+polylength(x_inter[0],x_inter[1],p2)

N = 100
xmin = np.floor(x_inter[0]-1)
xmax = np.ceil(x_inter[1]+1)
x = np.linspace(xmin,xmax,N)

plt.figure()
y1 = np.polyval(p1,x)
y2 = np.polyval(p2,x)
plt.plot(x,y1,'r.',x,y2,'b.')

x_fill = np.linspace(x_inter[0],x_inter[1],N)
y_fill1 = np.polyval(p1,x_fill)
y_fill2 = np.polyval(p2,x_fill)
y_fill = np.append(y_fill1,y_fill2[::-1])
plt.fill(np.append(x_fill,x_fill[::-1]),y_fill,'g')
plt.title('Flaechenberechung und Umfang von Polynomen')
plt.xlabel('x')
plt.ylabel('y')
plt.text(-3,7,'A = ' + str(A))
plt.text(-3,-2,'C = ' + str(C))
plt.show()
