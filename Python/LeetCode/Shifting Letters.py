#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        len_shifts = len(shifts)
        for i in range(len_shifts - 2, -1, -1):
            shifts[i] = shifts[i] + shifts[i + 1]
        return "".join(chr((ord(S[i]) - 97 + shifts[i]) % 26 + 97) for i in range(len_shifts))


a = Solution()
b = a.shiftingLetters(
    S="abc", shifts=[3, 5, 9]
)
print(b)
