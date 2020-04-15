#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        listR = [0] + [-1] * (n - 1)    #record the shortest path
        listB = [0] + [-1] * (n - 1)
        setR = set([0])    #record visited nodes
        setB = set([0])
        edgeR = []   #record visited edges
        edgeB = []
        while len(edgeR) != len(red_edges) or len(edgeB) != len(blue_edges):
            isFin = True
            #Find Reds
            for x in red_edges:
                if x not in edgeR and x[0] in setB:
                    setR.add(x[1])
                    edgeR.append(x)
                    listR[x[1]] = listB[x[0]] + 1 if listR[x[1]] == -1 else min(listR[x[1]], listB[x[0]] + 1)
                    isFin = False
            #Find Blues
            for x in blue_edges:
                if x not in edgeB and x[0] in setR:
                    setB.add(x[1])
                    edgeB.append(x)
                    listB[x[1]] = listR[x[0]] + 1 if listB[x[1]] == -1 else min(listB[x[1]], listR[x[0]] + 1)
                    isFin = False
            if isFin:
                break
        ans = []
        for i in range(n):
            if listR[i] == -1:
                ans.append(listB[i])
            elif listB[i] == -1:
                ans.append(listR[i])
            else:
                ans.append(min(listR[i], listB[i]))
        return ans






a = Solution()
b = a.shortestAlternatingPaths(
    6,
    [[3, 4], [1, 5], [1, 0], [5, 3], [2, 1], [2, 0], [0, 3], [1, 2], [5, 2], [1, 4], [1, 3], [5, 0], [4, 5], [5, 5], [3, 3]],
    [[2, 5], [3, 0], [1, 2], [4, 3], [3, 4], [0, 4], [5, 0], [5, 2], [1, 0], [0, 2]]
)
print(b)
