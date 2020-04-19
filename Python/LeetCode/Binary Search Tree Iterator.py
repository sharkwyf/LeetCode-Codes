#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.path = []
        while root:
            self.path.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.path:
            res = self.path[-1]
            if res.right:
                node = res.right
                while node:
                    self.path.append(node)
                    node = node.left
            else:
                last = self.path.pop()
                while self.path:
                    if self.path[-1].left == last:
                        break
                    last = self.path.pop()
            return res.val
        else:
            return None

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.path) > 0


# Your BSTIterator object will be instantiated and called as such:

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a1.right = a3
obj = BSTIterator(a1)
param_1 = obj.next()
param_2 = obj.hasNext()
param_3 = obj.next()
param_4 = obj.hasNext()
param_5 = obj.next()
param_6 = obj.hasNext()


# a = Solution()
# b = a.expressiveWords(
#     "zzzzzyyyyy",
#     ["zzyy", "zy", "zyy"]
# )
# print(b)