"""
nums = [5, -3, 10, -8, 0, 2]
- Return square roots of only positive numbers
"""

import math

nums = [5, -3, 10, -8, 0, 2]
m = list(map(lambda x: math.sqrt(x), filter(lambda x: x>=0, nums)))
print(m)
