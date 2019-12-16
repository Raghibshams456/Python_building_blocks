"""
Create a custom dtype that describes a color as four unsigned bytes (RGBA)
"""

import numpy as np
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])
                  

"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\019_numpy_custom_dtype.py                 .\019_numpy_custom_dtype.py:9: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
  ("a", np.ubyte, 1)])
PS C:\Users\SP\Desktop\DiveintoData\Numpy>   
"""