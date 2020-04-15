#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def cuttingRope(self, n: int) -> int:
        dic = {2: 1, 3: 2, 4: 4}
        if n in dic:
            return dic[n]
        a, b = n // 3, n % 3
        if b == 0:
            res = pow(3, a)
        elif b == 1:
            res = pow(3, a - 1) * 4
        else:
            res = pow(3, a) * 2
        return res % 1000000007




a = Solution()
b = a.cuttingRope(
   1000
)
print(b)
