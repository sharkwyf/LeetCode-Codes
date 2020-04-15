#!/usr/bin/python3
# Filename: test.py
from typing import List
from collections import Counter


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        maxN = -1
        for i in range(0, len(arr)):
            maxN = max(maxN, arr[i])
            if maxN == i:
                res += 1
        return res


a = Solution()
b = a.maxChunksToSorted(
    [1,0,2,3,4]
)
print(b)
