#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        return min(x[0] for x in ops) * min(x[1] for x in ops)


a = Solution()
b = a.maxCount(
        3,
    3,
    []
)
print(b)
