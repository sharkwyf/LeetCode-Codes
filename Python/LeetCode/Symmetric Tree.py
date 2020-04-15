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

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def DFSTransverse(root: TreeNode, direction: bool) -> List:
            if root:
                return [root.val] + \
                     ((DFSTransverse(root.left, direction) + DFSTransverse(root.right, direction)) if direction else \
                    (DFSTransverse(root.right, direction) + DFSTransverse(root.left, direction)))
            else:
                return [None]

        return DFSTransverse(root, True) == DFSTransverse(root, False)

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a1.right = a3


a = Solution()
b = a.isSymmetric(
    a1
)
print(b)
