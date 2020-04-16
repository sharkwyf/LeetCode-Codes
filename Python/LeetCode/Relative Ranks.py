#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        arr = [[n, i] for i, n in enumerate(nums)]
        arr.sort(reverse=True)
        res = [""] * len(nums)
        for i, x in enumerate(arr):
            if i == 0:
                res[x[1]] = "Gold Medal"
            elif i == 1:
                res[x[1]] = "Silver Medal"
            elif i == 2:
                res[x[1]] = "Bronze Medal"
            else:
                res[x[1]] = str(i + 1)
        return res



a = Solution()
b = a.findRelativeRanks(
    [5, 4, 3, 2, 1]
)
print(b)
