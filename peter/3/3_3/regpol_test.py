# test fuer regpol
#==============================================================================
# typ : String, Typ des Polyeders ('t','w','o','d' bzw. 'i')  
# a   : Vektor, Kantenlaenge des Polyeders  
# V   : Vektor, Volumen des Polyeders  
# F   : Vektor, Oberflaeche des Polyeders  
# R   : Vektor, Radius der umschreibenden Kugel  
# r   : Vektor, Radius der einbeschriebenen Kugel  
#==============================================================================
from regpol import *
import numpy as np

# dafa
a=3.
(V,F,R,r) = regpol('W',a)

a=3. 
(V,F,R,r) = regpol('Wuerfel',a) 

a=1. 
(V,F,R,r) = regpol('w',a) 
k=np.arange(1,4, dtype = 'float')  
(V,F,R,r) = regpol('w',k) 

a=2. 
(V,F,R,r) = regpol('d',a) 
k=np.arange(1,5, dtype = 'float')  
(V,F,R,r) = regpol('d',k) 

a=3.
(V,F,R,r) = regpol('i',a) 
k=np.arange(1,5, dtype = 'float')  
(V,F,R,r) = regpol('i',k) 

a=4.
(V,F,R,r) = regpol('o',a) 
k=np.arange(1,5, dtype = 'float')  
(V,F,R,r) = regpol('o',k) 

a=2.
(V,F,R,r) = regpol('t',a) 
k=np.arange(1,4, dtype = 'float') 
(V,F,R,r) = regpol('t',k) 
