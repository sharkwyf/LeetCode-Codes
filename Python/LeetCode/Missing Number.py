#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums)
        return len_nums * (len_nums + 1) // 2 - sum(nums)


a = Solution()
b = a.missingNumber(
    [9,6,4,2,3,5,7,0,1]
)
print(b)
