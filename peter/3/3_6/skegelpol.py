# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 21:47:27 2013

@author: Peter
"""
import numpy as np
import matplotlib.pyplot as plt
from ellipse import *
from hyperbel import *
n_points = 300  
a = 3  
b = 2  
r_0 = 6 

pi= np.pi
NaN = np.NaN
# Achsenkreuz
r_achse = np.array([r_0,r_0,np.NaN,r_0,r_0])
p_achse = np.array([-pi,0,np.NaN,-pi/2,pi/2])

# Kasten
x_k = np.array([a,-a,-a,a,a]) 
y_k = np.array([b,b,-b,-b,b] )
r_k = np.sqrt(x_k**2 + y_k**2) 
p_k = np.arctan2(y_k,x_k) 

# Asymptote
r_asym = np.array([r_0,r_0,NaN,r_0,r_0] )
x_asym = np.array([a,-a,NaN,a,-a])
y_asym = np.array([b,-b,NaN,-b,b])
p_asym = np.arctan2(y_asym,x_asym) 

# Ellipse
[phi,r] = ellipse(n_points,a,b) 
plt.figure()
plt.polar(p_achse,r_achse,'r')

plt.polar(p_k,r_k,'r')
plt.polar(phi,r) 

plt.title(['Ellipse: ','a=',str(a),' b=',str(b)]) 
#print('-depsc2','k_ellipse.eps')
#print('-dpng','k_ellipse.png')


# Hyperbel
[phi,r] = hyperbel(n_points,a,b,r_0) 
plt.figure ()
plt.polar(p_achse,r_achse,'r')

plt.polar(p_k,r_k,'r')
plt.polar(p_asym,r_asym,'g')
plt.polar(phi,r) 
plt.polar(pi-phi,r) 

plt.title(['Hyperbel: ','a=',str(a),' b=',str(b)]) 
#print('-depsc2','k_hyperbel.eps')
#print('-dpng','k_hyperbel.png')
plt.show()
