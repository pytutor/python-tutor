# -*- coding: utf-8 -*-

import numpy as np
import regpol 
Kante = np.arange(1,4)

(Volumen_d, x, x, x)=regpol.regpol('Dodekaeder',Kante)
(Volumen_w,Flaeche_w, x, x)=regpol.regpol('Wuerfel',Kante)
(Volumen_o,Flaeche_o,Radius_o,x )=regpol.regpol('Oktaeder',Kante)
(x,Flaeche_i,Radius_i,radius_i)=regpol.regpol('Ikosaeder',Kante)
(x,x,Radius_t,radius_t)=regpol.regpol('Tetraeder',Kante)