#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x for x in s.lower() if x.isalnum()]
        return not s or all(s[i] == s[-(i + 1)] for i in range(len(s) // 2))


a = Solution()
b = a.isPalindrome(
    "A man, a plan, a canal: Panama1"
)
print(b)
