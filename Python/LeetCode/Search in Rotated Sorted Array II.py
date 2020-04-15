#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def DFS(nums: List[int], target: int) -> bool:
            if not nums:
                return False
            low, high = 0, len(nums) - 1
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[low] == nums[mid] == nums[high]:
                return DFS(nums[1: mid], target) or DFS(nums[mid + 1: high], target)
            elif nums[low] <= target <= nums[mid] or target < nums[mid] < nums[low] or nums[mid] <= nums[high] < target:
                return DFS(nums[:mid], target)
            else:
                return DFS(nums[mid + 1:], target)

        return DFS(nums, target)


a = Solution()
b = a.search(
    [3, 1, 1], 3
)
print(b)
