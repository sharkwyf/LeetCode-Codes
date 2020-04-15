#!/usr/bin/python3
# Filename: test.py
from functools import lru_cache
from typing import List
import re

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = {}
        x = headA
        while x:
            seen[x] = None
            x = x.next
        x = headB
        while x:
            if x in seen:
                return x
            else:
                x = x.next
        return


a = Solution()
b = a.hIndex(
    intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
)
print(b)
