#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt = 0
        dict = collections.defaultdict(list)
        dict[0].append(-1)
        for i in range(len(nums)):
            cnt += nums[i]
            dict[2 * cnt - i - 1].append(i)
        m = 0
        for x in dict.values():
            m = max(m, x[-1] - x[0])
        return m


a = Solution()
b = a.findMaxLength(
    [0,1,0]
)
print(b)
