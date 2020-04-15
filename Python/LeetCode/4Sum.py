#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNSum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:  # early termination
                return
            if N == 2:
                low, high = 0, len(nums) - 1
                while low < high:
                    s = nums[low] + nums[high]
                    if s < target:
                        low += 1
                    elif s > target:
                        high -= 1
                    else:
                        results.append(result + [nums[low], nums[high]])
                        low += 1
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
            else:
                for i in range(0, len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        findNSum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)
            return

        results = []
        nums.sort()
        findNSum(nums, target, 4, [], results)
        return results


a = Solution()
b = a.fourSum(
    [1, 0, -1, 0, -2, 2],
    0
)
print(b)
