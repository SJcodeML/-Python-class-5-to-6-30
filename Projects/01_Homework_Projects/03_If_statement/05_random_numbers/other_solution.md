"""
solution 2 :
Using a loop (same behavior, more explicit)    


import random

values = []
for _ in range(10):
    values.append(random.randint(1, 100))
print(values)

------------------------------------
solution#3a : 
Using a list comprehension (each run produces 10 numbers, values may repeat)
python
import random

values = [random.randint(1, 100) for _ in range(10)]
print(values)

-----------
solution#3b :
Approach B: shuffle a list and slice

import random

nums = list(range(1, 101))
random.shuffle(nums)
values = nums[:10]
print(values)


------------------------------------
solution#4 : 

If you prefer using NumPy (faster for large arrays or scientific use)
import numpy as np

values = np.random.randint(1, 101, size=10)
print(values)

