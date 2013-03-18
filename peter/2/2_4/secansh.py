import numpy as np
from hyperbolic_secant import *
# Funktion: sgauss
# Aufruf: g = sgauss(x,x_0,s)
# Berechnet fuer den Vektor x die Werte der Gaussfunktion mit dem Maximum 
# bei x_0 und mit der Halbwertsbreite s
# Input:  Vektor x, Skalar x_0, Skalar s
# Output: Vektor g(x)
#
# Name: Peter Boehling
# nach dem Matalabskript von Winfried Kernbichler

def secansh(x,x_0,s):
    pi = np.pi


    h = 1 / pi / s * hyperbolic_secant( -(x-x_0) / s)
    return(h)
