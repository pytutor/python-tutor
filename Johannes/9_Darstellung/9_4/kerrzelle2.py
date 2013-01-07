# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 10:54:29 2012

@author: johannes
"""

import numpy as np
import pylab as plt

data = np.loadtxt('kerrtab-pu.dat')

u2 = data[:,0]
phi_gruen = data[:,1]
d_phi_gruen = data[:,2]
phi_gelb = data[:,3]
d_phi_gelb = data[:,4]
phi_blau = data[:,5]
d_phi_blau = data[:,6]

plt.figure()
plt.errorbar(u2,phi_gruen,d_phi_gruen,fmt='g*')
plt.errorbar(u2,phi_gelb,d_phi_gelb,fmt='y.')
plt.errorbar(u2,phi_blau,d_phi_blau,fmt='bx')
plt.grid('on')

N = 100
x = np.linspace(0,1.1*u2.max(),N)

c_gruen = sum(u2*phi_gruen)/sum(u2**2)
c_gelb = sum(u2*phi_gelb)/sum(u2**2)
c_blau = sum(u2*phi_blau)/sum(u2**2)

print('U² Abhaengigkeit von phi fuer gruenes Licht: ' + str(c_gruen))
print('U² Abhaengigkeit von phi fuer gelbes Licht: ' + str(c_gelb))
print('U² Abhaengigkeit von phi fuer blaues Licht: ' + str(c_blau))

plt.xlabel('$U^2$')
plt.ylabel('$\Delta \phi$')
plt.plot(x,c_gruen*x,'g')
plt.plot(x,c_gelb*x,'y')
plt.plot(x,c_blau*x,'b')
plt.title('Linearer Fit')
plt.legend(('gruen','gelb','blau'),loc='upper left')
plt.savefig('spannungsabhaengigkeit.eps',dpi=300)
plt.show()