#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = collections.Counter(arr)
        len_a = len(arr)
        cnt = 0
        for i, item in enumerate(c.most_common()):
            cnt += item[1]
            if cnt >= len_a / 2:
                return i + 1



a = Solution()
b = a.minSetSize(
    [1, 9]
)
print(b)
