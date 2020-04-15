#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, x in enumerate(nums):
            if target - x in s:
                return [s[target - x], i]
            else:
                s[x] = i

a = Solution()
b = a.twoSum(
    nums = [3, 3], target = 6,
)
print(b)
