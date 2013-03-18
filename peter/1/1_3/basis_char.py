# Zeichenketten
import numpy as np
s1 = 'a'
s2 = 'b'
s3 = [s1,s2]

c1 = 'das'
c2 = 'ist'
c3 = 'eine'
c4 = 'wunderbare'
c5 = 'uebung'

leer = ' '
ruf = '!'

C1 = c1
C1 = C1.title()
C5 = c5
C5 = C5.title()


satz = C1 + leer + c2 + leer + c3 + leer + c4 + leer + C5 + ruf

class_satz = type(satz)
class_zahl = type(12)

laenge_satz = len(satz)
