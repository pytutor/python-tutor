# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:32:37 2013

@author: pboehling
"""

#version: P2

# M hat 6 bis 12 Zeilen und 7 bis 11 Spalten

import numpy as np
# Info
M = np.random.rand(8,12)
ndim = np.ndim(M)
lenght = len(M)
siz = np.shape(M)
num = np.size(M)

# Skalare
n1 = M[5,4]
n2 = M[6]
n3 = M[-1]
n4 = M[-1-1]

# zeilenvektoren
z1 = M[3:8] 
z2 = M[1:5:-1]
z3 = M[([(1)],[(8)],[(6)] )]
z4 = M[[2,-1-1]]
z5 = M[3:end-2]
z6 = M[4,:]
z7 = M[1:end]
z8 = M[end:-1:1]
z9 = M[[1,2,2,3,3,3]]

# Spaltenvektoren
s1 = M[:]
s2 = M[:,5]
s3 = M[:,end-1]
s4 = M[1:end-1,end-1]
s5 = M[end:-1:1,2]
s6 = M[end:-1:1].T()
s7 = M[:,ceil[end/2]]

# Matrizen
m1 = M[3:5,:]
m2 = M[1:2:end,:]
m3 = M[:,2:end-1]
m4 = M[1:3:end,1:2:end]
m5 = M[[2,end-1],[2,end-1]]
m6 = M[[4,4,4],:]
m7 = M[end:-1:1,3:-1:2]
m8 = M[ceil[end/2]-1:ceil[end/2]+1,ceil[end/2]-1:ceil[end/2]+1]

# Ersetzungen
M1 = M 
M1[1:2:end] = NaN
M2 = M 
M2[1:2:end,:] = NaN
M3 = M 
M3[2:end-1,end-1] = 0

