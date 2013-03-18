#==============================================================================
# 
# Name: datentypen.py                                             
# Beschreibung: Einfuehrungsbeispiel zum Thema Klassen(Datentypen)
# Fundamentale Datentypen in Matlab, Cast, Befehl type, gemischte
# Ausdruecke                                                      
# Autor: Peter  Boehling                                   
# Datum: 23.01.2013                                              
# 
# 
# %Definition von Variablen unterschiedlicher Datentypen
#==============================================================================
import numpy as np
a=np.int8(65)
b=np.uint8(77)
c=np.uint16(84)
d=76
e=65
f=np.int(66)

#Feststellung des Datentyps einer Variablen (type)

typ_a=type(a)
typ_b=type(b)
typ_c=type(c)
typ_d=type(d)
typ_e=type(e)
typ_f=type(f)

#Casts auf andere Datentypen (z.B. str)

str_a=str(a)
str_b=str(b)
str_c=str(c)
str_d=str(d)
str_e=str(e)
str_f=str(f)

wort=str([a,b,c,d,e,f])

#Gefahren bei Casts auf andere Datentypen

test1=1.8e-60
test2=1.4
test3=1.5
test4=128

cast_test1=np.int(test1)
cast_test2=np.uint8(test2)
cast_test3=np.uint8(test3)
cast_test4=np.uint8(test4)
cast_test5=np.int8(test4)

