#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def DFS(seen: List[List[int]], board: List[List[str]], word: str) -> bool:
            if not word:
                return True
            else:
                for off in offset:
                    x, y = seen[-1][0] + off[0], seen[-1][1] + off[1]
                    if 0 <= x < height and 0 <= y < width:
                        if [x, y] not in seen and board[x][y] == word[0]:
                            seen.append([x, y])
                            if DFS(seen, board, word[1:]):
                                return True
                            else:
                                seen.pop()
            return False

        if not board or not board[0] or not word:
            return False
        height, width = len(board), len(board[0])
        offset = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    if DFS([[i, j]], board, word[1:]):
                        return True
        return False


a = Solution()
b = a.exist(
    board = [["a","b"],["c","d"]], word = "abcd"
)
print(b)
