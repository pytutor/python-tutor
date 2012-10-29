import numpy as np
import matplotlib.pyplot as plt

x_start = -5;
x_end = 5;
x_delta = 0.5;

x_1 = np.arange(x_start, x_end+1);
y_1 = x_end * abs(x_1);

x_2 = np.arange(x_start, x_delta, x_end);
y_2 = x_2 ** 2;

fig = plt.gcf()
plt.plot(x_1,y_1,'r-o',x_2,y_2,'b-o')
plt.show()
