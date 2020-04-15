#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        l, r = 0, 0
        res = 0
        for i in range(len(A)):
            if i > 0 and min(A[i], B[i]) > max(A[i-1], B[i-1]):
                res += min(l, r)
                if A[i] > B[i]:
                    l, r = 1, 0
                elif A[i] < B[i]:
                    l, r = 0, 1
                else:
                    l, r = 0, 0
            else:
                if A[i] < B[i]:
                    r += 1
                elif A[i] > B[i]:
                    l += 1
        res += min(l, r)
        return res



a = Solution()
b = a.minSwap(
    A = [1,3,5,4,5,6,7,8], B = [1,2,3,7,8,9,10,11]
)
print(b)