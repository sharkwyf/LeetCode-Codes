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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = 0
        head = cur = ListNode(0)
        while c or l1 or l2:
            value = (l1.val if l1 else 0) + \
                    (l2.val if l2 else 0) + \
                    c
            c = value > 9
            value %= 10
            if l1:
                l1.val = value
                cur.next = l1
            elif l2:
                l2.val = value
                cur.next = l2
            else:
                cur.next = ListNode(value)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        cur.next = None
        return head.next


a = Solution()
b = a.pushDominoes(
    ".L.R...LR..L.."
)
print(b)
