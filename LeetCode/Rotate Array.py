#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenN = len(nums)
        count = 0
        for i in range(0, k):
            if count >= lenN:
                break
            start = i
            next = (i + k) % lenN
            count += 1
            while start != next:
                nums[start], nums[next] = nums[next], nums[start]
                next = (next + k) % lenN
                count += 1
        return


a = Solution()
b = a.rotate(
    [1, 2, 3, 4, 5, 6],
4
)
print(b)
