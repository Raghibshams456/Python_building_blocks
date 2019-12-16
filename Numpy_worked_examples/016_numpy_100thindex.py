"""
Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
"""

import numpy as np
print(np.unravel_index(99,(6,7,8)))


"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\016_numpy_100thindex.py                   
(1, 5, 3)
PS C:\Users\SP\Desktop\DiveintoData\Numpy>                                                                                                
"""