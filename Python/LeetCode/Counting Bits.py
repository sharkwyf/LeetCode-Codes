#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i // 2] + i % 2
        return res


a = Solution()
b = a.countBits(
    8
)
print(b)
