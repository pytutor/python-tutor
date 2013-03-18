# Geschachteltes if 
import numpy as np
a = 1
b = 2

s = np.sign(a*b) # Vorzeichen -1,0,+1
if s > 0:
    if a > 0:
        print('1-Zweig: beide > 0')
    else:
        print('1-Zweig: beide < 0')
    
elif s < 0:
    print('1-Zweig: unterschiedliche Vorzeichen')
else:
    print('1-Zweig: zumindest eine 0')
