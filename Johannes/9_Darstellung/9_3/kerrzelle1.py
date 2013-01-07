# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 10:34:00 2012

@author: johannes
"""

import numpy as np
import pylab as plt

data = np.loadtxt('kerrtab.dat')

phi = data[:,0]/360*(2*np.pi);
I_lin = data[:,1]
I_zirk = data[:,2]
I_ellip = data[:,3]

plt.figure()
plt.polar(phi,I_lin,'r*')
plt.polar(phi,I_zirk,'bo')
plt.polar(phi,I_ellip,'kx')

plt.title('Winkelabhaengigkeit der Intensitaet')
plt.legend(('linear','zirkular','elliptisch'))

#savefig muss vor show() ausgefuehrt werden
plt.savefig('winkelabhaengigkeit.eps',dpi=300)
plt.show()