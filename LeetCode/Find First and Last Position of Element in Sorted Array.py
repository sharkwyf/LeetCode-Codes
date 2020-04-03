#!/usr/bin/python3
# Filename: test.py
from typing import List
from collections import Counter


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lenN = len(nums)
        low, high = -1, lenN
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid
        c0 = high
        low, high = -1, lenN
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid
            else:
                high = mid
        c1 = low
        return [c0, c1] if c0 <= c1 else [-1, -1]


a = Solution()
b = a.searchRange(
    [1], 1
)
print(b)
