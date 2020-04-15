#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for x in nums:
            a ^= x
        return a



a = Solution()
b = a.singleNumber(
    [4,1,2,1,2]
)
print(b)