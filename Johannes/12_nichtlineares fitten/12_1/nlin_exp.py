# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:13:49 2013

@author: johannes
"""
#http://lister.dulci.duhs.duke.edu/~cliburn/summer-school/python/_build/html/model_fitting.html

import numpy as np
import pylab as plt
from scipy import optimize

f = lambda beta,t: np.exp(-t*beta)

data = np.loadtxt('daten_nlin_exp.dat')
t = data[:,0]
y = data[:,1]

beta_opt = optimize.curve_fit(f,t,y)[0][0]

plt.figure()
plt.plot(t,y,'b*')
tt = np.linspace(0,15,300)
plt.plot(tt,f(beta_opt,tt),'k')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Daempfungsfaktor = ' + str(beta_opt))
plt.ylim((-0.1,1.1))
plt.show()