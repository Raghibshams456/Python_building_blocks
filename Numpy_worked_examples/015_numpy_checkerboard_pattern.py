"""
Create a 8x8 matrix and fill it with a checkerboard pattern
"""

import numpy as np

Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)


"""

PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\015_numpy_checkerboard_pattern.py         [[0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]]
PS C:\Users\SP\Desktop\DiveintoData\Numpy>  

"""