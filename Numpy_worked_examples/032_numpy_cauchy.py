"""
Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))
"""

import numpy as np
X = np.arange(8)
Y = X + 0.5
C = 1.0 / np.subtract.outer(X, Y)
print(np.linalg.det(C))


"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\032_numpy_cauchy.py                       
3638.163637117973
PS C:\Users\SP\Desktop\DiveintoData\Numpy>  
"""
