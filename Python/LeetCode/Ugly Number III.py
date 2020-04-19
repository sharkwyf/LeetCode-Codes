#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def LCM(x: int, y: int) -> int:
            return x * y // GCD(x, y)

        def GCD(x: int, y: int) -> int:
            minor = x if x < y else y
            if x % minor == y % minor == 0:
                return minor
            for i in range(int(minor ** 0.5 // 1), 0, -1):
                if x % i == y % i == 0:
                    return i

        lcmab = LCM(a, b)
        lcmbc = LCM(b, c)
        lcmca = LCM(c, a)
        lcm = LCM(lcmab, c)
        low, high = 1, 2 * (10 ** 9)
        while low < high:
            mid = (low + high) // 2
            count = mid // a + mid // b + mid // c - mid // lcmab - mid // lcmbc - mid // lcmca + mid // lcm
            if count >= n:
                high = mid
            else:
                low = mid + 1
        return low


a = Solution()
b = a.nthUglyNumber(
7,
7,
7,
7
)
print(b)
