#!/usr/bin/python3
# Filename: test.py
from typing import List
import math

class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        t = math.ceil(math.log(n, 2) + 1)
        arr = [pow(2, x) for x in range(0, t)]
        while n > 1:
        
        return t

a = Solution()
b = a.integerReplacement(
    24
)
print(b)
