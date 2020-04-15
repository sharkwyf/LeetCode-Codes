#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        lenA = len(arr)
        if lenA < 2:
            return False
        s = set()
        for x in arr:
            if x * 2 in s or (x % 2 == 0 and x // 2 in s):
                return True
            s.add(x)
        return False


a = Solution()
b = a.checkIfExist(
    [-3, -3, 19, 2, -16]
)
print(b)
