"""
onsider a generator function that generates 10 integers and use it to build an array 
"""

import numpy as np
def generate():
    for x in range(10):
        yield x
Z = np.fromiter(generate(),dtype=float,count=-1)
print(Z)

"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\027_numpy_array_from_function.py          [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
PS C:\Users\SP\Desktop\DiveintoData\Numpy>   
"""