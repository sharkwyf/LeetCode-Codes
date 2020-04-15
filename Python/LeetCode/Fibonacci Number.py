#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def fib(self, N: int) -> int:
        prev, cur = 0, 1
        for i in range(N):
            prev, cur = cur, prev + cur
        return prev


a = Solution()
b = a.fib(
    4
)
print(b)
