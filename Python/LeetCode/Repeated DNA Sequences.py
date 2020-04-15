#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res, r = set(), set()
        for i in range(0, len(s) - 9):
            [r, res][s[i:i+10] in r].add(s[i:i+10])
        return res


a = Solution()
b = a.findRepeatedDnaSequences(

"AAAAAAAAAAA"
)
print(b)
