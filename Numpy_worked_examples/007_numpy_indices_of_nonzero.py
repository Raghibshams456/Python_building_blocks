"""
Find indices of non-zero elements from [1,2,0,0,4,0] 
"""

import numpy as np

nz = np.nonzero([1,2,0,0,4,0])
print(nz)



"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\007_numpy_indices_of_nonzero.py           (array([0, 1, 4], dtype=int64),)
PS C:\Users\SP\Desktop\DiveintoData\Numpy>   
"""