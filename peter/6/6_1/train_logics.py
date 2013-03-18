# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:31:26 2013

@author: Peter
"""

# A, B, C are given
# Variables
# L_ass1,L_ass2,L_comm1,L_comm2,L_abs1,L_abs2,L_dist1,L_dist2
# L_comp1,L_comp2,L_ide1,L_ide2,L_bound10,L_bound11,L_bound20,L_bound21
# L_inv,L_mor1,L_mor2,L_1,L_2,L_12

# associativity
import numpy as np
import numpy.random as random

A = (random.rand(7,7))
B = (random.rand(7,7))
C = (random.rand(7,7))

L_ass1 = ( A or (B or C) ) == ( (A or B) or C )
L_ass2 = ( A and (B and C) ) == ( (A and B) and C )

# commutativity
L_comm1 = ( A or B ) == ( B or A )
L_comm2 = ( A and B ) == ( B and A )

# absorbtion
L_abs1 = ( A or (A and B) ) == A
L_abs2 = ( A and (A or B) ) == A

# distributivity
L_dist1 = ( A or (B and C) ) == ( (A or B) and (A or C) )
L_dist2 = ( A and (B or C) ) == ( (A and B) or (A and C) )

# complements
L_comp1 = ( A or ~A ) == 1
L_comp2 = ( A and ~A ) == 0

# idempotency
L_ide1 = ( A or A ) == A
L_ide2 = ( A and A ) == A

# boundedness
L_bound10 = ( A or 0 ) == A
L_bound11 = ( A or 1 ) == 1
L_bound21 = ( A and 1 ) == A
L_bound20 = ( A and 0 ) == 0

# involution
L_inv = ~~A == A

# de Morgan's laws
L_mor1 = ~(A or B) == (~A and ~B)
L_mor2 = ~(A and B) == (~A or ~B)


L_1 = ~( (A and B) or (A and C) or (B and C) )
L_2 = (~A or ~B) and (~A or ~C) and (~B or ~C)
L_12 = all(L_mor1[:]==L_mor2[:])

