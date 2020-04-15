#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        arr = [0] * (len(S) + 1)
        for i in range(len(S)):
            arr[-i - 2] = arr[-i - 1] + int(S[-i - 1]) * (2 ** i)
        seen = set()
        for i in range(1, math.floor(math.log(N, 2)) + 2):
            for j in range(0, len(S) - i + 1):
                seen.add((arr[j] - arr[j + i]) // (2 ** (len(S) - j - i)))
        return all(x in seen for x in range(1, N + 1))


a = Solution()
b = a.queryString(
    "1", 1
)
print(b)
