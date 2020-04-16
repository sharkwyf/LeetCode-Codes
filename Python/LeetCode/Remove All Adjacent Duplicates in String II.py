#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        dic = []
        for x in s:
            if dic and dic[-1][0] == x:
                dic[-1][1] += 1
                if dic[-1][1] == k:
                    dic.pop()
            else:
                dic.append([x, 1])
        if dic and dic[-1][1] >= k:
            dic.pop()
        return "".join(x[0] * x[1] for x in dic)


a = Solution()
b = a.removeDuplicates(
    s = "deeedbbcccbdaa", k = 3
)
print(b)
