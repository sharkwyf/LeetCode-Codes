#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for x in words:
            for i in range(1, len(x)):
                s.discard(x[i:])
        return sum(len(x) + 1 for x in s)


a = Solution()
b = a.minimumLengthEncoding(
    words = ["time", "atime", "btime"]
)
print(b)