"""
Given a 1D array, negate all elements which are between 3 and 8, in place
"""

import numpy as np
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)

"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\021_numpy_negate_matrix.py                [ 0  1  2  3 -4 -5 -6 -7 -8  9 10]
PS C:\Users\SP\Desktop\DiveintoData\Numpy>    
"""