"""
add a border (filled with 0's) around an existing array
"""

import numpy as np
Z = np.ones((5,5))
print("before adding border: ", Z)
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print("After adding border: ", Z, sep = '\n')



"""

PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\013_numpy_borderofones.py                 
before adding border:  
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
After adding border:
[[0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0.]]
PS C:\Users\SP\Desktop\DiveintoData\Numpy>  
"""