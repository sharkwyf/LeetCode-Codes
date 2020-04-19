#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a, b = num + 1, num + 2
        r = int(b ** 0.5 // 1)
        while r > 0:
            if a % r == 0:
                return [r, a // r]
            elif b % r == 0:
                return [r, b // r]
            else:
                r -= 1





a = Solution()
b = a.closestDivisors(
    123
)
print(b)
