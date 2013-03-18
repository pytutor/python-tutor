# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:40:41 2013

@author: Peter
"""
import numpy as np

L1 = M > 9                               
anz_L1 = np.sum(L1(:)) 
L2 = M >= 7 & M <= 24                
anz_L2 = np.sum(L2(:)) 
L3 = mod(M,6) == 0                       
anz_L3 = sum(L3(:)) 
L4 = mod(M,7) == 0 & mod(M,5) == 0  
anz_L4 = sum(L4(:)) 
L5 = mod(M,7) == 0 | mod(M,5) == 0  
anz_L5 = sum(L5(:)) 
L6 = mod(M,6) ~= 0                       
anz_L6 = sum(L6(:)) 
L7 = M > mean(M(:))                         
anz_L7 = sum(L7(:)) 
L8 = M >= (60/100) * max(M(:))            
anz_L8 = np.sum(L8(:)) 

anz_L1_L5 = np.sum(L1(:) & L5(:)) 

w_L5 = M(L5) 
w_L8 = M(~L8) 
w_L1_L3 = M(L1(:) & L3(:)) 

i2 = np.find(L2) 
[iz2,is2] = np.find(L2) 

M8 = M  
M8(L8) = 68 
M4 = M  
M4(L4) = 2 * M4(L4) 
M7 = M  
M7(L7) = mean(M(:))+1  
M7(~L7) = np.mean(M(:))-1 

eines_L3  = np.any(L3(:)) 
keines_L3 = np.~any(L3(:)) 
alle_L2 = np.all(L2(:)) 
nicht_alle_L2   = np.~all(L2(:)) 