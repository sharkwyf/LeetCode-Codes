#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        else:
            # Row
            for i in range(len(grid)):
                cnt = 0
                first = None
                for j in range(len(grid[0])):
                    if grid[i][j] > 0:
                        cnt += 1
                        first = j if first is None else first
                        if cnt > 1:
                            grid[i][j] = 2
                if cnt > 1:
                    grid[i][first] = 2
            # Column
            for i in range(len(grid[0])):
                cnt = 0
                first = None
                for j in range(len(grid)):
                    if grid[j][i] > 0:
                        cnt += 1
                        first = j if first is None else first
                        if cnt > 1:
                            grid[j][i] = 2
                if cnt > 1:
                    grid[first][i] = 2
            return sum(1 for y in grid for x in y if x == 2)


a = Solution()
b = a.countServers(
    [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
)
print(b)
