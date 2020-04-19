#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if len(numbers) < 3:
            return min(numbers)
        mid = (len(numbers) - 1) // 2
        if numbers[0] < numbers[mid]:
            m1 = numbers[0]
        else:
            m1 = self.minArray(numbers[:mid])
        if numbers[mid] < numbers[-1]:
            m2 = numbers[mid]
        else:
            m2 = self.minArray(numbers[mid + 1:])
        return min(m1, m2)


a = Solution()
b = a.minArray(
    [3,4,5,1,2]
)
print(b)
