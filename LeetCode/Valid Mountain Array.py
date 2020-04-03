#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) > 2 and A[1] > A[0]:
            is_up = True
        else:
            return False
        prev = A[1]
        for x in A[2:]:
            if x == prev or (not is_up and x > prev):
                return False
            elif is_up and x < prev:
                is_up = False
            prev = x
        return not is_up


a = Solution()
b = a.validMountainArray(
    [1, 3, 2]
)
print(b)
