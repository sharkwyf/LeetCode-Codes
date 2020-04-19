#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n % 2
            n //= 2
        return cnt


a = Solution()
b = a.hammingWeight(
   9
)
print(b)
