#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        ll, lr, rl, rr = None, None, None, None
        while head:
            if head.val < x:
                if lr:
                    lr.next = head
                    lr = lr.next
                else:
                    ll = head
                    lr = head
            else:
                if rr:
                    rr.next = head
                    rr = rr.next
                else:
                    rl = head
                    rr = head
            head = head.next
        if lr and rl:
            lr.next = rl
            rr.next = None
        return ll if ll else rl

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a6 = ListNode(6)
a6.next = a1
# a1.next = a5
a5.next = a2
a2.next = a4
a4.next = a3


a = Solution()
b = a.partition(
    a1, 0
)
print(b)
