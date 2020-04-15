#!/usr/bin/python3
# Filename: test.py
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        A, B = [l1, l2] if l1.val <= l2.val else [l2, l1]
        T, P = A, None
        while B:
            if T.val <= B.val:
                if not T.next:
                    T.next = B
                    break
                else:
                    P = T
                    T = T.next
            else:
                P.next = B
                B = B.next
                P = P.next
                P.next = T
        return A


a1 = ListNode(-9); a2 = ListNode(3); a3 = ListNode(4)
a1.next = a2; #a2.next = a3
b1 = ListNode(5); b2 = ListNode(7); b3 = ListNode(4)
b1.next = b2; #b2.next = b3


a = Solution()
b = a.mergeTwoLists(
    a1, b1
)
print(b)
