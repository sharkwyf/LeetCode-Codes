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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def build(arr: List[ListNode], low: int, high: int) -> TreeNode:
            if low >= high:
                return None
            else:
                mid = (low + high) // 2
                node = TreeNode(arr[mid].val)
                node.left = build(arr, low, mid)
                node.right = build(arr, mid + 1, high)
                return node

        arr = []
        while head:
            arr.append(head)
            head = head.next
        res = build(arr, 0, len(arr))
        return res


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a1.next = a2
a2.next = a3

a = Solution()
b = a.sortedListToBST(
    a1
)
print(b)
