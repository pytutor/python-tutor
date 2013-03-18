import numpy as np
import scipy.misc

q_1 = np.zeros(8)
q_2 = np.ones(7)
q_3 = 5*np.ones(6)

r_1 = np.arange(6)
r_2 = np.arange(0,6,0.5)
r_3 = np.arange(5,-1,-1)

s_1 = []

t_1 = np.linspace(0,5,90)
t_2 = np.linspace(5,0,80)

u_1 = np.logspace(-2,2,9)
u_2 = np.log10(u_1)

v_1 = np.exp(np.arange(-2,4))
v_2 = np.log(v_1)

w_1 = 2**np.arange(0,11)
w_2 = 1 / 2**np.arange(0,6)

x_1 = scipy.misc.factorial(np.arange(0,7))

y_1 = np.rand(10)
y_2 = np.randn(10)
y_3 = np.randint(5,15, size = 10)
