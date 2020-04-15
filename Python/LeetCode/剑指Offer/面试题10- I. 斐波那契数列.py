#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def fib(self, n: int) -> int:
        i = 0
        prev, next = 0, 1
        while i < n:
            prev, next = next, (prev + next) % 1000000007
            i += 1
        return prev


a = Solution()
b = a.fib(
45
)
print(b)
