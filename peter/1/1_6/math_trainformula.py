# Formeln zum Trainieren
import numpy as np
x         = np.pi/4
y         = np.pi/3

tan_x     = np.tan(x)
tan_y     = np.tan(y)
tan2_x    = tan_x**2

tan2_xp1    = tan2_x + 1
sq_tan2_xp1 = np.sqrt(tan2_xp1)

# Formeln

f_1    = tan_x / sq_tan2_xp1
f_2    = 1 / sq_tan2_xp1

f_3    = (tan_x + tan_y) / (1 - tan_x*tan_y)
f_4    = (tan_x - tan_y) / (1 + tan_x*tan_y)

f_5    = 2*tan_x / tan2_xp1
f_6    = (1 - tan2_x) / tan2_xp1


# x,y,tan_x,tan_y,tan2_x,tan2_xp1,sq_tan2_xp1,f_1,f_2,f_3,f_4,f_5,f_6