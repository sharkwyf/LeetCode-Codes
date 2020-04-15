#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        low, high = None, None
        profit = 0
        for i in range(len(prices)):
            if not low:
                low = prices[i]
            elif not high and prices[i] < low:
                low = prices[i]
            elif not high and low + fee < prices[i]:
                high = prices[i]
            elif high and high < prices[i]:
                high = prices[i]
            elif high and prices[i] + fee < high:
                profit += high - low - fee
                low, high = prices[i], None
            else:
                continue
        if low and high:
            profit += high - low - fee
        return profit


a = Solution()
b = a.maxProfit(
    [2, 1, 4, 4, 2, 3, 2, 5, 1, 2],
1
)
print(b)
