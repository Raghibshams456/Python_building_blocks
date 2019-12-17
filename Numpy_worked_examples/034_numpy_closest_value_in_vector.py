"""
How to find the closest value (to a given scalar) in a vector?
"""

import numpy as np

Z = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(Z-v)).argmin()
print(Z[index])


"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\034_numpy_closest_value_in_vector.py      
10
PS C:\Users\SP\Desktop\DiveintoData\Numpy>                                                                                                 
"""