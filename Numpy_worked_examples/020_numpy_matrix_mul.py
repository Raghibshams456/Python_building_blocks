"""
Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
"""

import numpy as np

Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)


"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\020_numpy_matrix_mul.py                   
[[3. 3.]
 [3. 3.]
 [3. 3.]
 [3. 3.]
 [3. 3.]]
PS C:\Users\SP\Desktop\DiveintoData\Numpy> 
"""