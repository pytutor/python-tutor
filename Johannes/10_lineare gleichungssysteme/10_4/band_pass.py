# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:06:08 2012

@author: johannes
"""

import numpy as np
import matplotlib.pyplot as plt

RLC_func = lambda om,R,L,C: np.array([[-1,1,1,0,0],\
                                       [0,1,0,-1,1],\
                                       [om*L[0]*1j + 1/(1j*om*C[0]),0,0,1j*om*L[1],0],\
                                       [0,0,0,1j*om*L[1],1/(1j*om*C[1])],\
                                       [0,0,1j*om*L[2] + 1/(1j*om*C[2]) + R[2],0,1/(1j*om*C[1])],\
                                       ])
    
u = 1
R = np.array([np.nan,np.nan,1])
L = C = np.ones(3)                                    
U = np.array([0,0,u,0,0])        
N = 201
om_v = np.logspace(-1,1,N)

I = np.zeros([5,N],dtype=complex)

for i in range(N):
    I[:,i] = np.linalg.solve(RLC_func(om_v[i],R,L,C),U)
    
plt.figure()
plt.subplot(211)
plt.semilogx(om_v,abs(I[2,:]))
plt.title('Amplitude')
plt.xlabel('$\Omega$')
plt.ylabel('$|I_3|$')
plt.subplot(212)
plt.semilogx(om_v,np.angle(I[2,:]))
plt.title('Phase')
plt.xlabel('$\Omega$')
plt.ylabel('$\Theta$')
plt.ylim((-np.pi,np.pi))
plt.tight_layout() # um zu verhindern, dass title und xlabel überlappen
plt.show()