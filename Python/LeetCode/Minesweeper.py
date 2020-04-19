#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    _offset = [
        [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1],[1, -1], [1, 0], [1, 1]
    ]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def reveal(board: List[List[str]], cord: List[int]) -> None:
            if board[cord[0]][cord[1]] != "E":
                return
            cnt = 0
            for off in self._offset:
                i, j = cord[0] + off[0], cord[1] + off[1]
                if 0 <= i < len(board) and 0 <= j < len(board[0]):
                    if board[i][j] == "M":
                        cnt += 1
            if cnt > 0:
                board[cord[0]][cord[1]] = str(cnt)
            else:
                board[cord[0]][cord[1]] = "B"
                for off in self._offset:
                    i, j = cord[0] + off[0], cord[1] + off[1]
                    if 0 <= i < len(board) and 0 <= j < len(board[0]):
                        reveal(board, [i, j])
            return

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        else:
            reveal(board, click)
        return board



a = Solution()
b = a.updateBoard(
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'M', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']],
    [1,2]
)
print(b)
