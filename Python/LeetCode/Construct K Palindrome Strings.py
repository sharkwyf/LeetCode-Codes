#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        dic = collections.defaultdict(bool)
        for x in s:
            dic[x] = not dic[x]
        cnt = 0
        for key in dic:
            cnt += dic[key]
            if cnt > k:
                return False
        return len(s) >= k





a = Solution()
b = a.canConstruct(
    "qlkzenwmmnpkopu",
    15
)
print(b)
