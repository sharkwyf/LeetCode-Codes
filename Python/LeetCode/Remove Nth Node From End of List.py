#!/usr/bin/python3
# Filename: test.py
from typing import List
from collections import Counter


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ptr = head
        cur = head
        while cur.next:
            if n == 0:
                ptr = ptr.next
            else:
                n -= 1
            cur = cur.next
        if n == 0:
            ptr.next = ptr.next.next
        elif n == 1:
            head = head.next
        return head


a = Solution()
a1 = ListNode(1)
a2 = ListNode(2); a1.next = a2
a3 = ListNode(3); a2.next = a3
a4 = ListNode(4); a3.next = a4
a5 = ListNode(5); a4.next = a5
b = a.removeNthFromEnd(
a1, 2
)
print(b)
