#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odds = sum(1 for c in chips if c % 2 == 1)
        return min(odds, len(chips) - odds)



a = Solution()
b = a.possibleBipartition(
4,
[[1,2],[1,3],[2,4]]
)
print(b)
