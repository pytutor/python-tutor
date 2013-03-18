import numpy as np
# Funktion: sgauss
# Aufruf: g = sgauss(x,x_0,s)
# Berechnet fuer den Vektor x die Werte der Gaussfunktion mit dem Maximum 
# bei x_0 und mit der Halbwertsbreite s
# Input:  Vektor x, Skalar x_0, Skalar s
# Output: Vektor g(x)
#
# Name: Peter Boehling
# nach dem Matalabskript von Winfried Kernbichler
def sgauss(x,x_0,s):
    pi = np.pi
    sqrt = np.sqrt
    exp = np.exp
    g = 1 / sqrt(2*pi) / s * exp( -(x-x_0)**2 / 2 / s**2 )
    return(g)