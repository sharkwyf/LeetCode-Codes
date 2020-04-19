#!/usr/bin/python3
# Filename: test.py
from typing import List
from collections import Counter


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lenN = len(nums)
        dict = {}
        isContained = False
        for i in range(0, min(lenN, k)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        if k >= lenN:
            return any(dict[x] > 1 for x in dict)
        else:
            for i in range(k, lenN):
                if nums[i] in dict:
                    if dict[nums[i]] > 0:
                        isContained = True
                        break
                    else:
                        dict[nums[i]] += 1
                else:
                    dict[nums[i]] = 1
                dict[nums[i - k]] -= 1
        return isContained


a = Solution()
b = a.containsNearbyDuplicate(
[99,99],
2
)
print(b)
