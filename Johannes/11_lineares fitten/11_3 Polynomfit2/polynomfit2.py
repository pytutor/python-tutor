# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 14:27:55 2012

@author: johannes
"""

import numpy as np
import pylab as plt

data = np.loadtxt('polydat.dat')
x = data[:,0]
y = data[:,1]
dy = data[:,2]

N = 100

plt.figure()
plt.errorbar(x,y,dy,fmt='g*')

#Gleichung zu lösen: y = A*p mit A = [[1,x,x²,x³]] und p = [[p_0...p_3]]
#A = np.vstack([np.ones(x.shape),x]).T # da 2. und 3. Ordnung vorgegeben
#p = np.linalg.lstsq(A,y)[0]
#pol = np.append(p,[-3.2,1])
#pol = pol[::-1]


p_2 = -3.2
p_3 = 1
X = np.vstack([np.ones(x.shape),x]).T
a = np.linalg.lstsq(X,(y-(p_2*x**2)-(p_3*x**3)))[0]
pol = [p_3,p_2,a[1],a[0]]


x_fit = np.linspace(1.1*min(x),1.1*max(x),N)
y_fit = np.polyval(pol,x_fit)
plt.plot(x_fit,y_fit,'r')
plt.grid()
plt.title('Polynomfit mit festen Koeffizienten')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(('Messdaten','$p_0+p_1*x-3.2*x^2+1*x^3$'))
plt.show()