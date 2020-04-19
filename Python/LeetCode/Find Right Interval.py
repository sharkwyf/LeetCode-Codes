#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i in range(len(intervals)):
            intervals[i].append(i)
        intervals.sort(key=lambda x: x[0])
        res = [-1] * len(intervals)
        for i in range(len(intervals)):
            l, h = i + 1, len(intervals)
            while l < h:
                mid = (l + h) // 2
                if intervals[mid][0] < intervals[i][1]:
                    l = mid + 1
                elif intervals[mid][0] == intervals[i][1]:
                    l = h = mid
                else:
                    h = mid
            if l < len(intervals):
                res[intervals[i][2]] = intervals[l][2]
        return res


a = Solution()
b = a.findRightInterval(
    [[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]
)
print(b)
