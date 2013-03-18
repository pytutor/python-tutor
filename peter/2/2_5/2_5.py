# Version: 1
import numpy as np

x= input('Bitte geben Sie x ein: ')
y= input('Bitte geben Sie y ein: ')
eps = 2.2204e-016
#Vorbereitung
left = np.zeros((7), dtype= 'complex')
right = np.zeros((7),dtype= 'complex')

# Berechnungen

left[0]  = np.log(x/y)
right[0] = np.log(x) - np.log(y)

left[1]  = np.exp(-1j*x)
right[1] = np.cos(x) - 1j*np.sin(x)

left[2]  =np.exp(x-y) 
right[2] = np.exp(x) / np.exp(y)

left[3]  = np.cosh(x+y) 
right[3] = np.cosh(x)*np.cosh(y) + np.sinh(x)*np.sinh(y)

left[4]  = np.sinh(x);
right[4] = (np.exp(1*x) - np.exp(-1*x)) / 2

left[5] = np.cos(2*x); 
right[5] = 2*np.cos(x)**2-1

left[6]  = np.sinh(2*x)
right[6] = 2*np.sinh(x)*np.cosh(x)

#Direkter Vergleich
v_exakt = left == right
v_eps   = abs(left-right) < 10*eps

print('Exakter Vergleich: ' + str(v_exakt))
print('Vergleich mit eps: ' + str(v_eps))
