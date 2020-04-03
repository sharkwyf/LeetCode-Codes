#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List
import re


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        x = head.val
        while head.next:
            head = head.next
            x = x * 2 + head.val
        return x

a1 = ListNode(1)
a2 = ListNode(0)
a1.next = a2

a = Solution()
b = a.getDecimalValue(
    a1
)
print(b)
