#!/usr/bin/python3
# Filename: test.py
import collections
from threading import Lock
from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        arr = []
        len_a, len_b = len(a), len(b)
        for i in range(max(len_a, len_b)):
            x = int(a[-(i + 1)]) if i < len_a else 0
            y = int(b[-(i + 1)]) if i < len_b else 0
            s = x + y + c
            c = s > 1
            arr.append(str(s - c * 2))
        if c:
            arr.append(str(1))
        return "".join(arr[::-1])


a = Solution()
b = a.addBinary(
    a = "1111", b = "1"
)
print(b)
