#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        indices = [i for i, v in enumerate(S) if v == C]
        res = []
        prev, next = None, 0
        for i, v in enumerate(S):
            if prev is None:
                res.append(indices[next] - i)
            elif next is None:
                res.append(i - indices[prev])
            else:
                res.append(min(indices[next] - i, i - indices[prev]))
            if next is not None and i == indices[next]:
                prev, next = next, next + 1 if next < len(indices) - 1 else None
        return res


a = Solution()
b = a.shortestToChar(
    S = "aaba", C = 'b'
)
print(b)
