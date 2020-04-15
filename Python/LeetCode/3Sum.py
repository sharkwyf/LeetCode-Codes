#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2:
            while 0 < i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
            l, h = i + 1, len(nums) - 1
            while l < h:
                s = nums[l] + nums[h]
                if -nums[i] < s:
                    h -= 1
                    while l < h and nums[h] == nums[h + 1]:
                        h -= 1
                else:
                    if -nums[i] == s:
                        res.append([nums[i], nums[l], nums[h]])
                    l += 1
                    while i < l < h and nums[l] == nums[l - 1]:
                        l += 1
            i += 1
        return res


a = Solution()
b = a.threeSum(
    [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
)
print(b)
