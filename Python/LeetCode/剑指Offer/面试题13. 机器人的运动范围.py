#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def DFS(matrix: List[List[int]], i: int, j: int, count: int) -> int:
            if not 0 <= i < m or not 0 <= j < n or matrix[i][j] != 0:
                return count
            x, y = i, j
            cnt = 0
            while x:
                cnt += x % 10
                x //= 10
            while y:
                cnt += y % 10
                y //= 10
            if cnt > k:
                matrix[i][j] = -1
            else:
                matrix[i][j] = 1
                count += 1
                count = DFS(matrix, i, j + 1, count)
                count = DFS(matrix, i, j - 1, count)
                count = DFS(matrix, i + 1, j, count)
                count = DFS(matrix, i - 1, j, count)
            return count

        if m * n == 0:
            return 0
        matrix = [[0 for i in range(n)] for i in range(m)]
        return DFS(matrix, 0, 0, 0)




a = Solution()
b = a.movingCount(
    m = 3, n = 1, k = 0
)
print(b)
