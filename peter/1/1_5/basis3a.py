# Version 1
# es gibt keine cotangens funktion in numpy
import numpy as np
import matplotlib.pyplot as plt

x_a = -3.0
x_e = 3.0
n   = 250

x = np.linspace(x_a,x_e,n)

y_sinh = np.sinh(x)
y_cosh = np.cosh(x)
y_tanh = np.tanh(x)
y_coth = (np.exp(2*x)+1)/(np.exp(2*x)-1)

plt.figure()
plt.plot(x,y_sinh,'k-')
plt.plot(x,y_cosh,'r-')
plt.plot(x,y_tanh,'g-')
plt.plot(x,y_coth,'b-')


plt.ylim([-max(y_sinh),max(y_sinh)])
plt.xlim([x_a,x_e])
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Hyperbolische Funktionen')

