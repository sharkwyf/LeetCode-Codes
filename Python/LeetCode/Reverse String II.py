#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s) // (2 * k)
        m = k // 2
        res = ""
        for i in range(n + 1):
            start = i * 2 * k
            if i < n:
                res += s[start:start + k][::-1] + s[start + k: start + 2 * k]
            elif len(s) - start <= k:
                res += s[start:][::-1]
            else:
                m = (len(s) - start) // 2
                res += s[start:start + k][::-1] + s[start + k:]
        return res


a = Solution()
b = a.reverseStr(
    "abcdefg", 2
)
print(b)
