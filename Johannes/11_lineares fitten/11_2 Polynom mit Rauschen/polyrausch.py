# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 14:08:10 2012

@author: johannes
"""

import numpy as np
import pylab as plt

p_test = np.array([-0.05,0.2,5,-1])
sigma = 5
N = 15
n = 100
x = np.linspace(-7,7,N)
y = np.polyval(p_test,x)

y = y + sigma * np.random.randn(y.shape[0])

plt.figure()
plt.errorbar(x,y,sigma,fmt='ro')
p_fit = np.polyfit(x,y,p_test.shape[0])

x_fit = np.linspace(2*min(x),2*max(x),n)
y_fit = np.polyval(p_fit,x_fit)
y_test = np.polyval(p_test,x_fit)
plt.plot(x_fit,y_fit,'g',x_fit,y_test,'b')

plt.grid()
plt.title('Test des Polynomfits')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(('Testdaten','Fitpolynom','Testpolynom'))
plt.show()