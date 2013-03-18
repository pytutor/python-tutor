# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 09:31:02 2013

@author: Peter
"""
import numpy as np
import numpy.random as random

mlt_r = random.rand(2)
mlt_nz = np.floor(mlt_r[0]*(7-4+1)) + 4
mlt_ns = np.floor(mlt_r[1]*(7-4+1)) + 4
if mlt_ns == mlt_nz:
    mlt_nz = mlt_nz + 1
M = random.rand(mlt_ns*mlt_nz*mlt_nz*mlt_ns)
M = M.reshape(mlt_nz*mlt_ns,mlt_nz,mlt_ns)



[nz,ns, nn] = np.shape(M)
nn = nz*ns*nn


sum_s1 = np.sum(M,axis = 0)
sum_s2 = np.sum(M,axis = 1)
sum_st = np.sum(M)

sum_f1 = np.zeros((np.shape(sum_s1)))
for kz in np.arange(nz):
    sum_f1 = sum_f1 + (M[kz,:,:])

sum_f2 = np.zeros((np.shape(sum_s2)))
for ks in np.arange(ns):
    sum_f2 = sum_f2 + (M[:,ks,:])

sum_ft = 0
for kn in np.arange(nn):
    sum_ft = sum_ft + M.reshape(mlt_nz*mlt_ns*mlt_nz*mlt_ns)[kn]

