#!/usr/bin/python3
# Filename: test.py
import collections
from threading import Lock
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def DFS(seen: List[List[int]], dict: collections.defaultdict, word: str, index: int) -> bool:
            if index >= len(word):
                return True
            for x in dict[word[index]]:
                if x not in seen and (not seen or abs(seen[-1][0] - x[0]) + abs(seen[-1][1] - x[1]) == 1):
                    seen.append(x)
                    if DFS(seen, dict, word, index + 1):
                        return True
                    seen.pop()
            return False

        if not board or not board[0]:
            return word is None
        seen = []
        dict = collections.defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in word:
                    dict[board[i][j]].append([i, j])
        return DFS(seen, dict, word, 0)

a = Solution()
b = a.exist(
    [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ],
    "ABCCED"
)
print(b)
