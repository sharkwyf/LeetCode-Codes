#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m, c = 0, 0
        for n in nums:
            if n:
                c += 1
            else:
                m = max(m, c)
                c = 0
        return max(m, c)


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a1.right = a3

a = Solution()
b = a.sumNumbers(
    a1
)
print(b)
