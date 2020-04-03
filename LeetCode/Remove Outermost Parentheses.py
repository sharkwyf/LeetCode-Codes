#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List
import re


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        arr = [0]
        cnt = 0
        for i in range(len(S)):
            if S[i] == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                arr.append(i + 1)
        return "".join(S[arr[i] + 1:arr[i+1] - 1] for i in range(len(arr) - 1))

a = Solution()
b = a.removeOuterParentheses(
    "(()())(())(()(()))"
)
print(b)
