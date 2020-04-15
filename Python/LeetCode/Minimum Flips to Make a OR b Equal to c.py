#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a > 0 or b > 0 or c > 0:
            ra, rb, rc = a % 2, b % 2, c % 2
            a, b, c = a // 2, b //2, c //2
            if rc == 0:
                count += ra + rb
            else:
                count += 1 if ra != 1 and rb != 1 else 0
        return count



a = Solution()
b = a.minFlips(
    1, 2, 3
)
print(b)
