# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:14:12 2013

@author: Peter
"""
import numpy as np
import matplotlib.pyplot as plt


datafile = 's_data_2d.dat'

arr=np.loadtxt(datafile)

xd = arr[:,0]
yd = arr[:,1]

ind = arr[:,0].argsort()
y = arr[ind,1]
x = arr[ind,0]

plt.figure()
plt.plot(xd,yd,'r:',x,y,'b-')
plt.show()