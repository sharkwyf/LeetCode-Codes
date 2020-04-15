#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        len_s = len(s)
        return any(all(s[j] == s[j - i - 1] for j in range(i + 1, len_s)) for i in range(len_s // 2) if s[i] == s[-1] and len_s % (i + 1) == 0)


a = Solution()
b = a.repeatedSubstringPattern(
    "abcabcabcabc"
)
print(b)
