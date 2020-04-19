#!/usr/bin/python3
# Filename: test.py
from functools import lru_cache
from typing import List
import re

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int) -> int:
            if i > 365:
                return 0
            elif i in days:
                return min(dp(i + 1) + costs[0], dp(i + 7) + costs[1], dp(i + 30) + costs[2])
            else:
                return dp(i + 1)
        return dp(1)


a = Solution()
b = a.mincostTickets(

    [1, 4, 6, 7, 8, 20],
    [2, 7, 15]
)
print(b)
