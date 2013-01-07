# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 10:48:53 2012

@author: johannes
"""

import numpy as np
import pylab as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


num_d = 5

xd = np.random.rand(num_d) - 0.5
yd = np.random.rand(num_d) - 0.5

M = np.transpose(np.array([xd**2 , 2*xd*yd , yd**2 , xd , yd , np.ones(num_d) ]))

n = int(np.floor(np.random.rand()*(num_d+1)))

logic = np.logical_not(np.ones(num_d+1))
logic[n] = True

b = -1 * M[:,logic]
D = M[:,np.logical_not(logic)]

s = np.linalg.solve(D,b)

s = np.insert(s,n,1)

#PLOT
anz = 30
x = y = np.linspace(-1,1,anz)
xx,yy = np.meshgrid(x,y)

zz = s[0]*xx**2 + s[1]*2*xx*yy + s[2]*yy**2 + s[3]*xx + s[4]*yy + s[5]
plt.figure()
plt.contour(xx,yy,zz,20, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=False)
#ax = fig.add_subplot(111,projection='3d')
#surf = ax.contour(xx,yy,zz)

plt.show()

#set(su_H,'EdgeColor','none') ;
#view(2)
#
#line(xd,yd,'Marker','o','Color','k','LineStyle','none');
#hold on
#v = [0,0]; contour(xx,yy,zz,v,'LineColor','black');
#hold off