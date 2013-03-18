# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:14:33 2013

@author: pboehling
"""
import numpy as np
import numpy.random as random
ze = np.zeros((3,5))
on = np.ones((3)) 
ey = np.eye((7))
di = np.diag((1,5)) 
ra = random.rand(5,3) 

ye = np.fliplr(ey) 
ide = np.flipud(di) 

col = ra.reshape(ra.shape[0]*ra.shape[1],1) 
row = ra.reshape(1,ra.shape[0]*ra.shape[1]) 

rep1 = np.tile(di,(1,2) )
rep2 = np.tile(di,(2,1)) 
rep3 = np.tile(di,(2,2) )

row_sum = np.sum(ra,axis = 0) 
col_sum = np.sum(ra,axis = 1) 
hide = 1 