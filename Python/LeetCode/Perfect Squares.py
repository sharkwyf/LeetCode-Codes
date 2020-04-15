#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


a = Solution()
b = a.numSquares(
    3102
)
print(b)
