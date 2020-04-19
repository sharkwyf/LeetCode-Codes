#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans = None
        while head:
            tmp = head
            head = head.next
            tmp.next = ans
            ans = tmp
        return ans


a = Solution()
b = a.validSquare(
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
)
print(b)
