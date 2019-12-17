"""
Extract the integer part of a random array using 5 different methods
"""

import numpy as np
Z = np.random.uniform(0,10,10)

print (Z - Z%1)
print (np.floor(Z))
print (np.ceil(Z)-1)
print (Z.astype(int))
print (np.trunc(Z))


"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\026_numpy_extract_int.py                  [0. 6. 1. 7. 5. 7. 4. 8. 0. 1.]
[0. 6. 1. 7. 5. 7. 4. 8. 0. 1.]
[0. 6. 1. 7. 5. 7. 4. 8. 0. 1.]
[0 6 1 7 5 7 4 8 0 1]
[0. 6. 1. 7. 5. 7. 4. 8. 0. 1.]
PS C:\Users\SP\Desktop\DiveintoData\Numpy>    
"""