#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def simplify(S: str) -> List:
            res = []
            i = 1
            last, cnt = S[0], 1
            while i < len(S):
                if S[i] == last:
                    cnt += 1
                else:
                    res.append([last, cnt])
                    last = S[i]
                    cnt = 1
                i += 1
            res.append([last, cnt])
            return res

        sample = simplify(S)
        cnt = 0
        for x in words:
            i, j, flag = 0, 0, True
            for s in sample:
                low = j
                while j < len(x):
                    if x[j] == s[0]:
                        j += 1
                    else:
                        break
                if (not s[1] >= j - low >= 1) \
                        or (s[1] == 2 != j - low):
                    flag = False
                    break
                i += 1
            cnt += flag
        return cnt


a = Solution()
b = a.expressiveWords(
    "zzzzzyyyyy",
    ["zzyy", "zy", "zyy"]
)
print(b)