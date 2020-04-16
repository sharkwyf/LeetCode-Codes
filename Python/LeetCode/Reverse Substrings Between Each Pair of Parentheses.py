#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s:
            return s
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                low = stack.pop()
                s = s[:low] + s[low:i + 1][::-1] + s[i + 1:]
        return s.replace("(", "").replace(")", "")


a = Solution()
b = a.reverseParentheses(
    "(ed(et(oc))el)"
)
print(b)
