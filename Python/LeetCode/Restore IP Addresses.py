#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        len_s = len(s)
        res = []
        for i in range(1, min(3, len_s - 3) + 1):
            if s[0] == "0" and i > 1:
                continue
            for j in range(i + 1, min(i + 3, len_s - 2) + 1):
                if s[i] == "0" and j > i + 1:
                    continue
                for k in range(j + 1, min(j + 3, len_s - 1) + 1):
                    if s[j] == "0" and k > j + 1:
                        continue
                    if s[k] == "0" and k < len_s - 1:
                        continue
                    if len_s - k > 3:
                        continue
                    elif int(s[0:i]) < 256 and int(s[i:j]) < 256 and int(s[j:k]) < 256 and int(s[k:]) < 256:
                        res.append(s[0:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:])
        return res


a = Solution()
b = a.restoreIpAddresses(
    "010010"
)
print(b)
