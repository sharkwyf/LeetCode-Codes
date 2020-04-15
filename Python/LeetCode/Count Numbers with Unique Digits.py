#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        cnt = 0
        for i in range(min(n + 1, 10)):
            c = 1
            for j in range(i):
                c *= min(9, 10 - j)
            cnt += c
        return cnt


a = Solution()
b = a.countNumbersWithUniqueDigits(
    1
)
print(b)
