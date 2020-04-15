#!/usr/bin/python3
# Filename: test.py
import collections
from threading import Lock
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        min_len = min(m, n)
        is_reversed = True
        for i in range(m + n - 1):
            item = []
            for j in range(0, min(i + 1, min_len, m + n - i - 1)):
                item.append(matrix[j + max(0, i - n + 1)][i - j - max(0, i - n + 1)])
            if is_reversed:
                res.extend(item[::-1])
            else:
                res.extend(item)
            is_reversed = not is_reversed
        return res

a = Solution()
b = a.findDiagonalOrder(
    [
     [ 1, 2 ],
     [ 4, 5],
     [ 7, 8 ]
    ]
)
print(b)
