# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:42:27 2013

@author: pboehling
"""

#Bedingte Schleife
#Gefahr: unendliche Schleife

n = 3

k = 0
while k < n: # solange Bedingung wahr ist
    k = k + 1
    print(['1: k = ',str(k)])


print(' ')

# oder
k = 0
while True:# Eigentlich fuer immer
    if k >= n:
        break # Ausstieg
    k = k + 1
    print(['2: k = ',str(k)])

    
print(' ')

# oder
k = 0
while True:  #Eigentlich fuer immer
    k = k + 1
    print(['3: k = ',str(k)])
    if k >= n:
        break #Ausstieg

    

    