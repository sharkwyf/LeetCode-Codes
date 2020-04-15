#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def is_match(s: str, p: str) -> bool:
            if not p:
                return not s
            elif p[0] != "*" and not s:
                return False
            else:
                if p[0] == ".":
                    return is_match(s[1:], p[1:])
                elif p[0] == "*":
                    if not p[1:]:
                        raise
                    i = 0
                    while i < len(s) + 1:
                        if is_match(s[i:], p[2:]):
                            return True
                        if p[1] != "." and (i < len(s) and p[1] != s[i]):
                            break
                        i += 1
                    return False
                else:
                    if s[0] == p[0]:
                        return is_match(s[1:], p[1:])
                    else:
                        return False

        return is_match(s[::-1], p[::-1])


a = Solution()
b = a.isMatch(
    "a",
"ab*a"
)
print(b)
