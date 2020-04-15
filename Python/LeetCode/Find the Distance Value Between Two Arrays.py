#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        arr2.append(1111)
        cnt = 0
        i, j = 0, 0
        for x in arr1:
            bottom, up = x - d, x + d
            while i < len(arr2) and arr2[i] < bottom:
                i += 1
            while j < len(arr2) and arr2[j] <= up:
                j += 1
            cnt += j == i
        return cnt


a = Solution()
b = a.findTheDistanceValue(
    [2, 1, 100, 3],
    [-5, -2, 10, -3, 7],
6
)
print(b)