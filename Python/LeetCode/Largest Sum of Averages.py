#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        lenA = len(A)
        P = [sum(A[0: i + 1]) for i in range(0, len(A))]
        li = [P[i] / (i + 1) for i in range(lenA)]
        for i in range(2, K + 1):
            for j in range(lenA - 1, 0, -1):
                li[j] = max(li[k] + (P[j] - P[k]) / (j - k) for k in range(0, j))
        return li[-1]


a = Solution()
b = a.largestSumOfAverages(
    [4, 1, 7, 5, 6, 2, 3],
4
)
print(b)
