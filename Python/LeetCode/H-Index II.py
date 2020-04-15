#!/usr/bin/python3
# Filename: test.py
from functools import lru_cache
from typing import List
import re

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        s = len(citations)
        if s == 0:
            return 0
        index = 0
        while index < s and citations[-(index + 1)] >= index + 1:
            c = citations[-(index + 1)]
            index += 1
        return index


a = Solution()
b = a.hIndex(

[0,0,4,4]
)
print(b)
