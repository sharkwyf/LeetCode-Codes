#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        return sum(1 for y in grid for x in y if x > 0) + \
              sum(max(y) for y in grid) + \
              sum(max(x) for x in zip(*grid))


a = Solution()
b = a.projectionArea(
    [[1, 2], [3, 4]]
)
print(b)
