#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        if len(ages) < 2:
            return 0
        l, m = 0, 0
        cnt = 0
        for h in range(1, len(ages)):
            while ages[l] <= 0.5 * ages[h] + 7 and l < h:
                l += 1
            if ages[h] <= 0.5 * ages[h] + 7:
                m = h
            else:
                while ages[m] != ages[h] and m < h:
                    m += 1
            cnt += 2 * h - l - m
        return cnt


a = Solution()
b = a.numFriendRequests(
    [73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]
)
print(b)
