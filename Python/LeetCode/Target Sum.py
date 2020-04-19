#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def find(nums: List[int], n: int, dp: List[dict], target: int) -> int:
            if target in dp[n]:
                pass
            elif n == len(nums):
                if target == 0:
                    dp[n][target] = 1
                else:
                    dp[n][target] = 0
            else:
                ans = find(nums, len(nums), dp, target)
                for i in range(n, len(nums)):
                    if target >= nums[i]:
                        ans += find(nums, i + 1, dp, target - nums[i])
                    else:
                        break
                dp[n][target] = ans
            return dp[n][target]

        nums.sort()
        S = S + sum(nums)
        for i in range(len(nums)):
            nums[i] *= 2
        dp = [{} for i in range(len(nums) + 1)]
        return find(nums, 0, dp, S)


a = Solution()
b = a.findTargetSumWays(
    [1, 1, 1, 1, 1],
3
)
print(b)
