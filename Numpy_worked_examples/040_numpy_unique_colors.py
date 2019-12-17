"""
Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors
"""

import numpy as np
w,h = 16,16
I = np.random.randint(0,2,(h,w,3)).astype(np.ubyte)
#Note that we should compute 256*256 first. 
#Otherwise numpy will only promote F.dtype to 'uint16' and overfolw will occur
F = I[...,0]*(256*256) + I[...,1]*256 +I[...,2]
n = len(np.unique(F))
print(n)


"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\040_numpy_unique_colors.py                8                                                                                        
"""