#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def DFS(Counter, lenA):
            if len(Counter.items()) == 0:
                return 1
            else:
                ans = 0
                item = Counter.popitem()
                for i in range(0, item[1] + 1):
                    ans += DFS(Counter, lenA + i) * C(i, lenA + i)
                Counter[item[0]] = item[1]
                return ans

        def C(i: int, length: int) -> int:
            r1, r2 = 1, 1
            for i in range(i):
                r1 *= i + 1
                r2 *= length - i
            return r2 // r1

        if not tiles:
            return 0
        return DFS(collections.Counter(tiles), 0) - 1


a = Solution()
b = a.numTilePossibilities(
    "AAB"
)
print(b)
