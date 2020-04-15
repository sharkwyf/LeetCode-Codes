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
        cnt = 1
        while n > 4:
            cnt *= 3
            n -= 3
        return cnt * n




a = Solution()
b = a.cuttingRope(
   2
)
print(b)
