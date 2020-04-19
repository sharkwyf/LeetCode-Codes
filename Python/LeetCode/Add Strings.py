#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        len1, len2 = len(num1), len(num2)
        i, c = 0, 0
        while i < len1 and i < len2 or c:
            s = (int(num1[- i - 1]) if i < len1 else 0) + (int(num2[- i - 1]) if i < len2 else 0) + c
            res.append(str(s % 10))
            c = s > 9
            i += 1
        return num1[:- i] + num2[:- i] + "".join(res[::-1])


a = Solution()
b = a.addStrings(
    "11111", "99"
)
print(b)
