#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            if x in s:
                return x
            else:
                s.add(x)
        return None


a = Solution()
b = a.restoreIpAddresses(
    "010010"
)
print(b)
