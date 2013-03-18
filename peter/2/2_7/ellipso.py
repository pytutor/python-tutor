import numpy as np
def ellipso(a,b):

    t=np.linspace(0,2*np.pi,100)
    x=a*np.cos(t)
    y=b*np.sin(t)
    
    return(x,y)