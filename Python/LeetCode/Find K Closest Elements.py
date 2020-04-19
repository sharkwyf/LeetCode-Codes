#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        i = 0
        for i in range(len(arr) - k):
            if arr[i] != arr[i + k] and abs(x - arr[i]) <= abs(arr[i + k] - x):
                break
        i += not abs(x - arr[i]) <= abs(arr[i + k] - x)
        return arr[i:i + k]


a = Solution()
b = a.findClosestElements(
    [1, 1, 1, 10, 10, 10],
1,
9
)
print(b)
