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
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            h = head.next
            del head
        else:
            h, prev, head = head, head, head.next
            while head:
                if head.val == val:
                    node = head
                    prev.next = node.next
                    del node
                    break
                head = head.next
                prev = prev.next
        return h


a1 = ListNode(4)
a2 = ListNode(5)
a3 = ListNode(1)
a4 = ListNode(9)
a1.next = a2
a2.next = a3
a3.next = a4

a = Solution()
b = a.deleteNode(
   a1, 0
)
print(b)
