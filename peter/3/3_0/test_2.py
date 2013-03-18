# Einfaches if mit and & bzw. or |

a = -1
b = 1

if a > 0 and b > 0:
    print('1-Zweig: beide > 0')
elif a < 0 and b < 0:
    print('1-Zweig: beide < 0')
elif (a < 0 and b > 0) or (a > 0 and b < 0):
    print('1-Zweig: unterschiedliche Vorzeichen')
else:
    print('1-Zweig: zumindest eine 0')
