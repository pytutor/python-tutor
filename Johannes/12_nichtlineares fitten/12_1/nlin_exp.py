# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:13:49 2013

@author: johannes
"""
#http://lister.dulci.duhs.duke.edu/~cliburn/summer-school/python/_build/html/model_fitting.html

import numpy as np
import pylab as plt
from scipy import optimize

def f(beta,t):
    return np.exp(-t*beta)

def resid(beta, y, t):
    return y - f(beta,t)

data = np.loadtxt('daten_nlin_exp.dat')
t = data[:,0]
y = data[:,1]

beta_start = 1
beta_opt,flag = optimize.leastsq(resid,beta_start,args=(y,t))

plt.plot(t,y,'*')
tt = np.linspace(0,15,300)
plt.plot(tt,f(beta_opt,tt),'k')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Daempfungsfaktor = ' + str(beta_opt[0]))
plt.ylim((-0.1,1.1))
plt.show()