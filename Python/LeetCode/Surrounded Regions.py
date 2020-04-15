#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def fix(row: int, col: int, board: List[List[str]]) -> None:
            if board[row][col] == "O":
                board[row][col] = "1"
                for off in offset:
                    if 0 <= row + off[0] < height and 0 <= col + off[1] < width:
                        fix(row + off[0], col + off[1], board)
            return

        if not board or not board[0]:
            return
        height, width = len(board), len(board[0])
        offset = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for j in range(width):
            fix(0, j, board)
            if height - 1 > 0:
                fix(height - 1, j, board)
        for i in range(1, height - 1):
            fix(i, 0, board)
            if width - 1 > 0:
                fix(i, width - 1, board)
        for i in range(height):
            for j in range(width):
                if board[i][j] == "1":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return


a = Solution()
matrix = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
b = a.solve(
    matrix
)
print(b)
