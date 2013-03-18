#Berechnung des Datums des Ostersonntags mit 
#Gauss'schen Osterformel

import numpy as np
X=input('Jahr fuer die Berechnung des Osterfestes:')
#Gauss'sche Zyklenzahl
a=np.mod(X,19)
b=np.mod(X,4)
c=np.mod(X,7)
k=np.fix(X/100)
p=np.fix((8*k+13)/25)
q=np.fix(k/4)
#Korr.: So- u. Mo-Gleichung
M=np.mod(15+k-p-q,30)
#Korr.: Sonnengleichung
N=np.mod(4+k-q,7)
#Mondentfernung
d=np.mod(19*a+M,30)
#Osterentfernung
e=np.mod(2*b+4*c+6*d+N,7)
Ostersonntag=(22+d+e)

if Ostersonntag <=31:
    Monat='Maerz'
else:
    Ostersonntag=Ostersonntag-31
    Monat='April'


print('Der Ostersonntag ist im Jahr ' + str(X)+' am '+str(Ostersonntag) +Monat)