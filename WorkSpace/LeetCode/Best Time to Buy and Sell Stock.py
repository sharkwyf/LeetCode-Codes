#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = []
        min = -1
        maxprofit = 0
        for x in prices:
            if x < min or min == -1:
                min = x
            if x - min > maxprofit:
                maxprofit = x - min
        return maxprofit



a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))
