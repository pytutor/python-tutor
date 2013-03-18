# if : keine Matrizen in Bedingungen erlaubt!

x = [1,-2, 7]

if x.all > 0:
    print('1-Zweig: alle Elemente > 0')
elif x.any > 0:
    print('1-Zweig: zumindest ein Element > 0')
else:
    print('1-Zweig: kein Element > 0')

#Python liefert keinen Fehler, wenn man beim ersten if schreibt:
#
#   if x > 0
#
# Daraus wird automatisch:
#
#   if all(x > 0)
#
#Man sollte das aber nicht tun!