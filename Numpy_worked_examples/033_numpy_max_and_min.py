"""
Print the minimum and maximum representable value for each numpy scalar type
"""

import numpy as np
for dtype in [np.int8, np.int32, np.int64]:
    print(np.iinfo(dtype).min)
    print(np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
    print(np.finfo(dtype).min)
    print(np.finfo(dtype).max)
    print(np.finfo(dtype).eps)
    
    

"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\033_numpy_max_and_min.py                  
-128
127
-2147483648
2147483647
-9223372036854775808
9223372036854775807
-3.4028235e+38
3.4028235e+38
1.1920929e-07
-1.7976931348623157e+308
1.7976931348623157e+308
2.220446049250313e-16
PS C:\Users\SP\Desktop\DiveintoData\Numpy>      
"""