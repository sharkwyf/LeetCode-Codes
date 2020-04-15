#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        last = intervals[0]
        res = 0
        for x in intervals[1:]:
            if x[0] < last[1]:
                if x[1] < last[1]:
                    last = x
                res += 1
            else:
                last = x
        return res


a = Solution()
b = a.eraseOverlapIntervals(
    [[1,2],[1,2],[1,2]]
)
print(b)
