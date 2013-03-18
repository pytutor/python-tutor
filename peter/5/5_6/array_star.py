# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 20:44:21 2013

@author: Peter
"""
import numpy as np

def array_star(m= None):

    if m == None:
        m=5
    
    M = np.diag(np.arange(1,m+1))
    A = np.array((M,np.fliplr(M) ,np.flipud(M),np.fliplr(np.flipud(M))))
    #A = np.reshape(np.hstack((A[0,:,:],A[1,:,:],A[2,:,:],A[3,:,:])), (2*m,2*m))
    A = np.hstack((A[0,:,:],A[1,:,:],A[2,:,:],A[3,:,:]))
    A = np.reshape(A, (2*m,2*m))
    
    return(A)


A = array_star(6)


print((A))
