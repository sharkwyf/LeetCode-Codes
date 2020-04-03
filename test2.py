#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        len_nums = len(nums)
        low, high = 0, len_nums - 1
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid] <= nums[high]:
                high = low
            elif nums[low] <= nums[mid]:
                low = mid
            elif nums[mid] <= nums[high]:
                high = mid
            else:
                raise
        arr = nums[high:] + nums[:high]
        l, r = 0, len_nums
        while l + 1 < r:

        return False


a = Solution()
b = a.search(
    nums=[2, 5, 6, 0, 0, 1, 2], target=1
)
print(b)
