#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1 / x, -n
        base = x
        res = base ** (n % 2)
        base = base * base
        n //= 2
        while n:
            if n % 2:
                res *= base
            base = base * base
            n //= 2
        return res


a = Solution()
b = a.myPow(
   2.00, 10
)
print(b)
