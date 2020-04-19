#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        min = count = S.count("0")
        for x in S:
            if x == "0":
                count -= 1
            elif x == "1":
                count += 1
            min = count if count < min else min
        return min


a = Solution()
print(a.minFlipsMonoIncr("00110"))
