#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return root
        else:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            if not root.left and not root.right and root.val == target:
                return None
            else:
                return root

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(2)
a1.left = a2
a2.right = a3


a = Solution()
b = a.removeLeafNodes(
    a1, 2
)
print(b)
