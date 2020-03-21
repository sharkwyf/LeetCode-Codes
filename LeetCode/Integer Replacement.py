#!/usr/bin/python3
# Filename: test.py
from typing import List
import math

class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        t = math.ceil(math.log(n, 2) + 1)
        arr = [pow(2, x) for x in range(0, t)]
        while n > 3:
            if n % 2 == 0:
                n /= 2
            else:
                if (n - 1) % 4 == 0:
                    n -= 1
                else:
                    n += 1
            count += 1
        if n == 3:
            n -= 1
            count += 1
        if n == 2:
            n /= 2
            count += 1
        return count


a = Solution()
b = a.integerReplacement(
    100
)
print(b)
