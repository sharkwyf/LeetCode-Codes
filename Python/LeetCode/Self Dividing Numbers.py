#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        is_self_deviding = lambda num: '0' not in str(num) and all(num % int(x) == 0 for x in str(num))
        return filter(is_self_deviding, range(left, right + 1))


a = Solution()
b = a.selfDividingNumbers(
    1, 22
)
print(b)
