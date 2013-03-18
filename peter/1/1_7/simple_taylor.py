# simple taylor
import numpy as np
from pylab import *

x_max = 2*np.pi 

x = np.linspace(-x_max,x_max,200)  
lim = 1.5  

y = np.sin(x)  
y1 = x  
y2 = - x**3 / 6  
y3 = + x **5 / 120  
y4 = - x **7 / 5040  



subplot(221)
plot(x,y,x,y1,'r--')
ylim([-lim, lim]) 
xlim([-x_max,x_max])
title('Entwicklung bis zum linearen Glied')
xlabel('x')  
ylabel('sin(x)')  

subplot(222)
plot(x,y,x,y1+y2,'r--')
ylim([-lim, lim]) 
xlim([-x_max,x_max])
title('Entwicklung bis zum kubischen Glied')
xlabel('x')  
ylabel('sin(x)')  

subplot(223)
plot(x,y,x,y1+y2+y3,'r--')
ylim([-lim ,lim]) 
xlim([-x_max,x_max])
title('Entwicklung bis zur Ordnung 5')
xlabel('x')  
ylabel('sin(x)')  

subplot(224)
plot(x,y,x,y1+y2+y3+y4,'r--') 
ylim([-lim ,lim]) 
xlim([-x_max,x_max])
title('Entwicklung bis zur Ordnung 7')
xlabel('x') 
ylabel('sin(x)') 
