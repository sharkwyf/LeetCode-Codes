#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def DFS(equations: List[List[str]], values: List[float], seen: List[str], node: str, query: List[str]) -> float:
            for i in range(len(equations)):
                if node == equations[i][0] and equations[i][1] not in seen:
                    if equations[i][1] == query[1]:
                        return values[i]
                    else:
                        seen.append(equations[i][1])
                        res = DFS(equations, values, seen, equations[i][1], query)
                        if res != -1.0:
                            return values[i] * res
                elif node == equations[i][1] and equations[i][0] not in seen:
                    if equations[i][0] == query[1]:
                        return 1 / values[i]
                    else:
                        seen.append(equations[i][0])
                        res = DFS(equations, values, seen, equations[i][0], query)
                        if res != -1.0:
                            return (1 / values[i]) * res
            return -1.0

        result = []
        s = set()
        for x in equations:
            s.add(x[0])
            s.add(x[1])
        for q in queries:
            if q[0] == q[1] and q[0] in s:
                result.append(1.0)
            else:
                result.append(DFS(equations, values, [q[0]], q[0], q))
        return result


a = Solution()
b = a.calcEquation(
    equations=[["b", "c"], ["b", "a"]],
    values=[3.0, 0.5],
    queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
)
print(b)
