# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 13:39:32 2012

@author: johannes
"""

import numpy as np
import pylab as plt

data = np.loadtxt('polydat1.dat')
x = data[:,0]
y = data[:,1]
dy = data[:,2]

plt.figure()
plt.errorbar(x,y,dy,fmt='g*')

pol0 = np.polyfit(x,y,0)
pol1 = np.polyfit(x,y,1)
pol2 = np.polyfit(x,y,2)
pol3 = np.polyfit(x,y,3)


N = 100
x_fit = np.linspace(1.1*min(x),1.1*max(x),N)
y_fit_0 = np.polyval(pol0,x_fit)
y_fit_1 = np.polyval(pol1,x_fit)
y_fit_2 = np.polyval(pol2,x_fit)
y_fit_3 = np.polyval(pol3,x_fit)
plt.plot(x_fit,y_fit_0,'b')
plt.plot(x_fit,y_fit_1,'r')
plt.plot(x_fit,y_fit_2,'k')
plt.plot(x_fit,y_fit_3,'c')
plt.grid()
plt.title('Polynomfit von Datenpunkten')
plt.legend(('Messdaten','p_0','p_0+p_1*x','p_0+p_1*x+p_2*x^2','p_0+p_1*x+p_2*x^2+p_3*x^3'),loc='lower right')
plt.show()