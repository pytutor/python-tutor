import numpy as np
def regpol(typ,a):
    
    #==============================================================================
    # typ : String, Typ des Polyeders ('t','w','o','d' bzw. 'i')  
    # a   : Vektor, Kantenlaenge des Polyeders  
    # V   : Vektor, Volumen des Polyeders  
    # F   : Vektor, Oberflaeche des Polyeders  
    # R   : Vektor, Radius der umschreibenden Kugel  
    # r   : Vektor, Radius der einbeschriebenen Kugel  
    #==============================================================================
    
    typ = typ.lower()
    if typ[0] == 't':
        V=a**3/12*np.sqrt(2) 
        F=a**2*np.sqrt(3) 
        R=a/4*np.sqrt(6) 
        r=a/12*np.sqrt(6) 
    elif typ[0] =='w':
        V=a**3 
        F=6*a**2 
        R=a/2*np.sqrt(3) 
        r=a/2 
    elif typ[0] =='o':
        V=a**3/3*np.sqrt(2) 
        F=2*a**2*np.sqrt(3) 
        R=a/2*np.sqrt(2) 
        r=a/6*np.sqrt(6) 
    elif typ[0] =='d':
        V=a**3/4*(15+7*np.sqrt(5)) 
        F=3*a**2*np.sqrt(5*(5+2*np.sqrt(5))) 
        R=a/4*(1+np.sqrt(5))*np.sqrt(3) 
        r=a/4*np.sqrt((50+22*np.sqrt(5))/5) 
    elif typ[0] =='i':
        V=5*a**3/12*(3+np.sqrt(5)) 
        F=5*a**2*np.sqrt(3) 
        R=a/4*np.sqrt(2*(5+np.sqrt(5))) 
        r=a/2*np.sqrt((7+3*np.sqrt(5))/6) 
    else:
        print('Unbekannter Typ')
    
    
    return(V,F,R,r)