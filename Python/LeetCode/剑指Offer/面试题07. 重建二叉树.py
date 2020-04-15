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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        idx = inorder.index(node.val)
        node.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        node.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return node


a = Solution()
b = a.replaceSpace(
"We are happy."
)
print(b)
