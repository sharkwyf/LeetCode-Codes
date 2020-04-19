#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def numTilings(self, N: int) -> int:
        res = [0] * max(N + 1, 4)
        res[0:4] = [1, 1, 2, 5]
        for i in range(4, N + 1):
            res[i] = (res[i - 1] * 2 + res[i - 3]) % 1000000007
        return res[N] if N > 0 else 0


a = Solution()
b = a.numTilings(
    30
)
print(b)
