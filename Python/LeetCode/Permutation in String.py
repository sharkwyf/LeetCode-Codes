#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tpl = collections.defaultdict(int)
        for c in s1:
            tpl[c] += 1
        sample = collections.defaultdict(int)
        for key in tpl:
            sample[key] = 0
        len_s1 = len(s1)
        for c in s2[:len_s1 - 1]:
            if c in sample:
                sample[c] += 1
        for i in range(len_s1 - 1, len(s2)):
            if s2[i] in sample:
                sample[s2[i]] += 1
                if sample == tpl:
                    return True
            if s2[i - len_s1 + 1] in sample:
                sample[s2[i - len_s1 + 1]] -= 1
        return False


a = Solution()
b = a.checkInclusion(
    s1 = "a",
    s2 = "ab"
)
print(b)
