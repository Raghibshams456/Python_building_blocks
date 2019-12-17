"""
Create an array class that has a name attribute
"""

import numpy as np
class NamedArray(np.ndarray):
    def __new__(cls, array, name="no name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        self.info = getattr(obj, 'name', "no name")

Z = NamedArray(np.arange(10), "range_10")
print (Z.name)


"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\039_numpy_arrayclass_name_attribute.py    range_10
PS C:\Users\SP\Desktop\DiveintoData\Numpy>  
"""