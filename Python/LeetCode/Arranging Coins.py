#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def arrangeCoins(self, n: int) -> int:
        t = int((n * 2) ** 0.5)
        return t if t * (t + 1) / 2 <= n else t - 1


a = Solution()
b = a.arrangeCoins(
    6
)
print(b)
