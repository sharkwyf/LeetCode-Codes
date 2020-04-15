#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            if S[i:i + len(s)] == s:
                S = S[:i] + t + S[i + len(s):]
        return S




a = Solution()
b = a.findReplaceString(
    S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
)
print(b)