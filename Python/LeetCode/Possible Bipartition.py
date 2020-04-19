#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def DFS(node: int, flag: True) -> bool:
            if (flag and edges[node][0] == 2) or (not flag and edges[node][0] == 1):
                return False
            elif edges[node][0] == 0:
                edges[node][0] = 1 if flag else 2
                for edge in edges[node][1:]:
                    if not DFS(edge, not flag):
                        return False
                return True
            else:
                return True

        if not dislikes:
            return True
        edges = [[0] for i in range(N + 1)]
        for edge in dislikes:
            edges[edge[0]].append(edge[1])
            edges[edge[1]].append(edge[0])
        for key in range(1, N + 1):
            if edges[key][0] == 0 and not DFS(key, True):
                return False
        return True





a = Solution()
b = a.possibleBipartition(
4,
[[1,2],[1,3],[2,4]]
)
print(b)
