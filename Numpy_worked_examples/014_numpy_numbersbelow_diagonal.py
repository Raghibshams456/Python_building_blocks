"""
Create a 5x5 matrix with values 1,2,3,4 just below the diagonal 
"""

import numpy as np
Z = np.diag(1+np.arange(4),k=-1)
print(Z)

"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\014_numpy_numbersbelow_diagonal.py        
[[0 0 0 0 0]
 [1 0 0 0 0]
 [0 2 0 0 0]
 [0 0 3 0 0]
 [0 0 0 4 0]]
PS C:\Users\SP\Desktop\DiveintoData\Numpy>  
"""