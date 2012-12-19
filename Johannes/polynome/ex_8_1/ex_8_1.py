# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:26:07 2012

@author: johannes
"""

import pylab as plt
import numpy as np

x=np.linspace(-5,4,400);
p3=np.array([1,6,-2,-20]);

y3=np.polyval(p3,x);
plt.plot(x,y3)

p2=p3[1:np.size(p3)];
y2=np.polyval(p2,x);


plt.plot(x,y2,'g')

p1=np.polyder(p2);
y1=np.polyval(p1,x);
plt.plot(x,y1,'r')

N=np.roots(p2);
plt.plot(N,[0,0],'g*')
plt.plot(plt.xlim(),[0,0],'k')

plt.legend(['kubisch','quadratisch mit Nullstellen','linear durch Ableitung'])
plt.title('verschiedene Polynomfunktionen')
plt.xlabel('x')
plt.ylabel('y')

plt.show()