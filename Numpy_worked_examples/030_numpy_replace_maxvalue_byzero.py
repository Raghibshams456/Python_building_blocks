"""
Create random vector of size 10 and replace the maximum value by 0
"""

import numpy as np
Z = np.random.random(10)
Z[Z.argmax()] = 0
print(Z)


"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\030_numpy_replace_maxvalue_byzero.py      [0.51217538 0.10107164 0.32605424 0.01094225 0.03380365 0.02556792
 0.37261103 0.14103957 0.         0.31710356]
PS C:\Users\SP\Desktop\DiveintoData\Numpy>                                                                                                  
"""