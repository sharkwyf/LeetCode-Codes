#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        len_n = len(nums)
        low, high = 0, len_n
        while low < high:
            mid = (low + high) // 2
            if mid + 1 < len_n and nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    low = mid + 2
                else:
                    high = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if mid % 2 == 0:
                    high = mid - 2
                else:
                    low = mid + 1
            else:
                return nums[mid]
        return nums[low]


a = Solution()
b = a.singleNonDuplicate(
    [1]
)
print(b)
