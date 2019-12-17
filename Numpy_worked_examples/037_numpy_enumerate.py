"""
What is the equivalent of enumerate for numpy arrays
"""

import numpy as np

Z = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(Z):
    print(index, value)
for index in np.ndindex(Z.shape):
    print(index, Z[index])
    
    

"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\037_numpy_enumerate.py                    
(0, 0) 0
(0, 1) 1
(0, 2) 2
(1, 0) 3
(1, 1) 4
(1, 2) 5
(2, 0) 6
(2, 1) 7
(2, 2) 8
(0, 0) 0
(0, 1) 1
(0, 2) 2
(1, 0) 3
(1, 1) 4
(1, 2) 5
(2, 0) 6
(2, 1) 7
(2, 2) 8
PS C:\Users\SP\Desktop\DiveintoData\Numpy>    
"""