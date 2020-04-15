#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if m == 0:
            return 1
        s = set()
        for i in range(2):
            for j in range(min(2, m - i + 1)):
                for k in range(min(2, m - i - j + 1)):
                    l = (m - i - j - k) % 2
                    cond = 2 ** n - 1
                    if i:
                        cond = 2 ** n - 1 - cond
                    if j:
                        ans = 0
                        for x in range(n):
                            if (n - x) % 2 == 0:
                                ans += (1 - (cond % 2)) * 2 ** x
                            else:
                                ans += (cond % 2) * 2 ** x
                            cond = cond // 2
                        cond = ans
                    if k:
                        ans = 0
                        for x in range(n):
                            if (n - x) % 2 == 1:
                                ans += (1 - (cond % 2)) * 2 ** x
                            else:
                                ans += (cond % 2) * 2 ** x
                            cond = cond // 2
                        cond = ans
                    if l:
                        ans = 0
                        for x in range(n):
                            if (n - x) % 3 == 1:
                                ans += (1 - (cond % 2)) * 2 ** x
                            else:
                                ans += (cond % 2) * 2 ** x
                            cond = cond // 2
                        cond = ans
                    if cond not in s:
                        s.add(cond)
        return len(s)


a = Solution()
b = a.flipLights(
    n = 2, m = 2
)
print(b)
