#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        lenA = len(A)
        if lenA == 1:
            return 0
        A.sort()
        for i in range(lenA):
            A[i] -= K
        minN, maxN = A[0], A[-1]
        sub = maxN - minN
        for i in range(lenA):
            A[i] += K * 2
            minN = A[0] if i == lenA - 1 else min(A[0], A[i + 1])
            maxN = A[i] if i == lenA - 1 else max(A[-1], A[i])
            sub = min(sub, maxN - minN)
        return sub


a = Solution()
b = a.smallestRangeII(

    [0, 10],2
)
print(b)
