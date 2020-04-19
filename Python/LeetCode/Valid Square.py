#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def is_vertical(p1: List[int], p2: List[int], q1: List[int], q2: List[int]):
            ans = (p1[0] - p2[0]) * (q1[0] - q2[0]) + (p1[1] - p2[1]) * (q1[1] - q2[1]) == 0
            return ans

        v = sorted([p1, p2, p3, p4])
        return v[0] != v[1] and v[1] != v[2] and v[2] != v[3] \
            and is_vertical(v[0], v[1], v[1], v[3]) \
            and is_vertical(v[1], v[3], v[3], v[2]) \
            and is_vertical(v[3], v[2], v[2], v[0]) \
            and is_vertical(v[2], v[0], v[0], v[1]) \
            and is_vertical(v[0], v[3], v[1], v[2])


a = Solution()
b = a.validSquare(
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
)
print(b)
