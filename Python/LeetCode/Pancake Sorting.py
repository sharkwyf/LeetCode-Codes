#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        n = len(A)
        while n > 1:
            maxindex = 0
            max = A[0]
            for i in range(0, n):
                if A[i] > max:
                    max = A[i]
                    maxindex = i
            if maxindex == n - 1:
                n -= 1
                continue
            if maxindex != 0:
                A = list(reversed(A[0: maxindex + 1])) + A[maxindex + 1:]
                ans.append(maxindex + 1)
            A = list(reversed(A[0:n]))
            ans.append(n)
            n -= 1
        return ans


a = Solution()
b = a.pancakeSort(
    [1, 2, 3, 4]
)
print(b)
