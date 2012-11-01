# unterschied arrays list
import numpy as np

list_type = range(10)
list_type_2 = range(1,10)
list_type_3 = range(0,10,2)

new_list = list_type*2
print(type(new_list))

array_type = np.arange(10)
array_type_2 = np.arange(1,10)
array_type_3 = np.arange(1,10,2)

new_array = array_type * 2
print(type(new_array))
