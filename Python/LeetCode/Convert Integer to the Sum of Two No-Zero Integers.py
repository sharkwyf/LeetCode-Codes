#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        l = r = re = i = 0
        while n > 0:
            re = n % 10
            n = n // 10
            if n > 0 and re <= 1:
                l += 9 * 10 ** i
                r += ((re - 9) % 10) * 10 ** i
                n -= 1
            else:
                l += 1 * 10 ** i
                r += (re - 1) * 10 ** i
            i += 1
        return [l, r]





a = Solution()
b = a.getNoZeroIntegers(
    n = 2000
)
print(b)
