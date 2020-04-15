#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        def DFS(bits_r: List[int]) -> bool:
            if not bits_r:
                return False
            elif len(bits_r) == 1:
                return bits_r[0] == 0
            else:
                if bits_r[0] == 0:
                    return DFS(bits_r[1:])
                elif bits_r[0] == 1:
                    return DFS(bits_r[2:])
                else:
                    return False

        return DFS(bits)



a = Solution()
b = a.isOneBitCharacter(

    [1, 1, 1, 0]
)
print(b)
