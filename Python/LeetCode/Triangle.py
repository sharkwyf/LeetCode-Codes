#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        for i in range(len(triangle) - 1):
            for j in range(len(triangle[- i - 2])):
                triangle[- i - 2][j] += min(triangle[- i - 1][j: j + 2])
        return triangle[0][0]



a = Solution()
b = a.minimumTotal(
    [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
)
print(b)
