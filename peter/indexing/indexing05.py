# indexing with masks

from numpy import *
from numpy import random
import matplotlib.pyplot as plt

number_of_values = 10000
x = random.random(number_of_values)
y = random.random(number_of_values)

y_mask = ma.masked_outside(y, 0.25 , 0.75)
x_mask = ma.masked_outside(x, 0.25 , 0.75)
mask_added = x_mask.mask + y_mask.mask

plt.figure()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('this is the title')
plt.legend(('unmaskiert', 'maskiert'))
plt.plot(x[mask_added], y[mask_added], 'bo', x[~mask_added], y[~mask_added], 'r*')
plt.show()
