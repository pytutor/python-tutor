# Einfaches if - Reihenfolge!

a = 1.5 

# Hier wird bei einfachen Zahlen nur ein Zweig ausgefuehrt

if a > 0:
    print('1-Zweig: a > 0')
elif a > 1:   # Zweig wird nie erreicht
    print('1-Zweig: a > 1')
elif a > 2:   # Zweig wird nie erreicht
    print('1-Zweig: a > 2')
else:
    print('1-Zweig: a <= 0')
  

print(' ')

  # andere Reihenfolge notwedig

if a > 2:
    print('2-Zweig: a > 2')
elif a > 1:
    print('2-Zweig: a > 1')
elif a > 0:
    print('2-Zweig: a > 1')
else:
    print('2-Zweig: a <= 0')
  

print(' ')

# oder Eingrenzen der Abfragen

if a > 0 and a <= 1:
    print('3-Zweig: a > 0')
elif a > 1 and a <= 2:
    print('3-Zweig: a > 1')
elif a > 2:
    print('3-Zweig: a > 2')
else:
    print('3-Zweig: a <= 0')
  

print(' ')

# oder mehrere Abfragen, dann sind auch mehrere Zweige moeglich 

if a >  0:
    print('4-Zweig: a > 0')     
if a >  1:
    print('4-Zweig: a > 1')     
if a >  2: 
    print('4-Zweig: a > 2')     
if a <= 0: 
    print('4-Zweig: a <= 0')    
