"""
Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates
"""

import numpy as np
Z = np.random.random((10,2))
X,Y = Z[:,0], Z[:,1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print(R)
print(T)


"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\029_numpy_cartesian_to_polar.py           [0.97368188 1.28829728 1.0891378  1.05497418 1.00455034 0.86839019
 1.11035987 0.40769622 0.78619998 0.16134067]
[0.11982595 0.7763605  0.88367566 0.63153008 1.20764353 1.19309996
 0.93808717 0.57978648 0.13407744 0.4288647 ]
PS C:\Users\SP\Desktop\DiveintoData\Numpy>  
"""