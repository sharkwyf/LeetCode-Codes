#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        self.data.append([x, min(x, self.data[-1][1]) if self.data else x])

    def pop(self) -> None:
        return self.data.pop()[0]

    def top(self) -> int:
        if self.data:
            return self.data[-1][0]

    def getMin(self) -> int:
        if self.data:
            return self.data[-1][1]


a = Solution()
b = a.arrayPairSum(
    [1,4,3,2]
)
print(b)