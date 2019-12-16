"""
get the dates of yesterday, today and tomorrow
"""

import numpy as np

yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today     = np.datetime64('today', 'D')
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')


print(yesterday)
print(today)
print(tomorrow)


"""
PS C:\Users\SP\Desktop\DiveintoData\Numpy> python .\023_numpy_dates.py                        2019-11-14
2019-11-15
2019-11-16
PS C:\Users\SP\Desktop\DiveintoData\Numpy> 
"""