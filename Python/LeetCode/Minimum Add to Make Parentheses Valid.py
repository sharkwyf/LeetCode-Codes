#!/usr/bin/python3
# Filename: test.py
import collections
from threading import Lock
from typing import List


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for x in S:
            if len(stack) and stack[-1] == "(" and x == ")":
                stack.pop()
            else:
                stack.append(x)
        return len(stack)


a = Solution()
b = a.minAddToMakeValid(
    "()))(("
)
print(b)
