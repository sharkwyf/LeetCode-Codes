#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        aa = 1
        digNumMin = len(str(low))
        digNumMax = len(str(high))
        min = low // pow(10, digNumMin - 1)
        max = high // pow(10, digNumMax - 1)

        for i in range(digNumMin, digNumMax + 1):
            for j in range(min if i == digNumMin else 1, ((max if max < (10 - i) else 10 - i) if i == digNumMax else (10 - i)) + 1):
                if i == digNumMin and j == min and sum(x * pow(10, digNumMin - x + j - 1) for x in range(j, j + digNumMin)) < low:
                    continue
                elif i == digNumMax and j == max and sum(x * pow(10, digNumMax - x + j - 1) for x in range(j, j + digNumMax)) > high:
                    continue
                else:
                    yield sum(x * pow(10, i - x + j - 1) for x in range(j, j + i))


a = Solution()
print(list(a.sequentialDigits(178546104, 812704742)))
