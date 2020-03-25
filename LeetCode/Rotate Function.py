#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        lenA = len(A)
        if lenA == 0:
            return 0
        list = []
        list.append(sum(i * A[i] for i in range(lenA)))
        s = sum(x for x in A)
        for i in range(1, lenA):
            list.append(list[i - 1] + s - lenA * A[-i])
        return max(list)



a = Solution()
b = a.maxRotateFunction(
    [4, 3, 2, 6]
)
print(b)
