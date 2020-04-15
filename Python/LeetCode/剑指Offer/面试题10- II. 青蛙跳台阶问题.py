#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def numWays(self, n: int) -> int:
        res = cnt = (n + 1) // 2 if n % 2 else 1
        for i in range(n % 2 + 2, n + 1, 2):
            cnt = (cnt * (n + i) // 2 * ((n + i) // 2 - i + 1) // i // (i - 1))
            res = (res + cnt)
        return res % 1000000007




a = Solution()
b = a.numWays(
48
)
print(b)
