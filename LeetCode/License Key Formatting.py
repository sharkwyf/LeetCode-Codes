#!/usr/bin/python3
# Filename: test.py
from typing import List
from collections import Counter


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()[::-1]
        return "-".join(S[i:i+K] for i in range(0, len(S), K))[::-1]



a = Solution()
b = a.licenseKeyFormatting(
    "5F3Z-2e-9-w", 3
)
print(b)
