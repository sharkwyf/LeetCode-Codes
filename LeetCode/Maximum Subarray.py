#!/usr/bin/python3
# Filename: test.py
from typing import List
from collections import Counter


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lenN = len(nums)
        if not lenN:
            return 0
        P = [0] * (lenN + 1)
        for i in range(lenN):
            P[i + 1] = P[i] + nums[i]
        minN = 0
        maxR = nums[0]
        for i in range(1, lenN):
            if P[i] < minN:
                minN = P[i]
            s = P[i + 1] - minN
            if s > maxR:
                maxR = s
        return maxR


a = Solution()
b = a.maxSubArray(
[-2, -3, -1]
)
print(b)
