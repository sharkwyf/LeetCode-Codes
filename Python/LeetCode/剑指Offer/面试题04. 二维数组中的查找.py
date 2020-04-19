#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        low, high = -1, len(matrix)
        while low + 1 < high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                high = mid
            else:
                low = mid
        matrix = matrix[:high]
        if not matrix:
            return False
        low, high = -1, len(matrix[0])
        while low + 1 < high:
            mid = (low + high) // 2
            if matrix[- 1][mid] == target:
                return True
            elif matrix[- 1][mid] > target:
                high = mid
            else:
                low = mid
        for i in range(len(matrix)):
            matrix[i] = matrix[i][high:]
        return self.findNumberIn2DArray(matrix, target)




a = Solution()
b = a.findNumberIn2DArray(
    [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ],
    0
)
print(b)
