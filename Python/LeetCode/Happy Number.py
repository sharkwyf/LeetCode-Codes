#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            arr = []
            while n != 0:
                arr.append(n % 10)
                n //= 10
            n = sum(pow(x, 2) for x in arr)
            if n == 1:
                return True
            elif n in s:
                return False
            else:
                s.add(n)



a = Solution()
b = a.isHappy(
19
)
print(b)
