#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.append(0)
        len_c = len(citations)
        for i in range(len_c):
            c = min(len_c - 1, citations[i])
            if c >= 0:
                citations[i] = -1
                while True:
                    t = citations[c]
                    if t < 0:
                        citations[c] -= 1
                        break
                    else:
                        citations[c] = -2
                        c = min(len_c - 1, t)
        cnt = len_c
        for i in range(len_c):
            cnt -= - 1 - citations[i]
            if cnt < i + 1:
                break
        return i


a = Solution()
b = a.hIndex(
    [0]
)
print(b)