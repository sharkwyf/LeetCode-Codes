#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) <= 3:
            return max(nums)
        li = [nums[1], nums[2], 0, nums[0], nums[0] + nums[2], nums[0]]
        for i in range(3, len(nums) - 1):
            li = [
                max(li[0:3]),
                max(li[0], li[2]) + nums[i],
                max(li[0], li[2]),
                max(li[3:6]),
                max(li[3], li[5]) + nums[i],
                max(li[3], li[5])
            ]
        i = len(nums) - 1
        return max(li[0] + nums[i], li[1], li[2] + nums[i], li[3], li[4], li[5])


a = Solution()
b = a.rob(

    [1, 2, 1, 1]
)
print(b)
