#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def DFS(m: List[List[int]]) -> List[int]:
            height = len(m)
            width = len(m[0]) if height > 0 else 0
            if height == 0 or width == 0:
                return []
            if height == 1:
                return m[0]
            elif width == 1:
                return [x[0] for x in m]
            else:
                return m[0] + [row[-1] for row in m[1:-1]] + m[-1][::-1] + [row[0] for row in m[-2:0:-1]] + DFS([row[1:-1] for row in m[1:-1]])

        return DFS(matrix)




a = Solution()
b = a.spiralOrder(
    [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
)
print(b)
