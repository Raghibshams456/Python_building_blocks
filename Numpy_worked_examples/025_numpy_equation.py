"""
How to compute ((A+B)*(-A/2)) in place (without copy)
"""

import numpy as np
A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)
print(A)


"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\025_numpy_equation.py                     [-1.5 -1.5 -1.5]
PS C:\Users\SP\Desktop\DiveintoData\Numpy>  
"""