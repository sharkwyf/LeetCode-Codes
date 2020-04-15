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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        arr1 = [root]
        arr2 = []
        res = [[root.val]]
        direction = True
        while (direction and arr1) or (not direction and arr2):
            ans = []
            if direction:
                while arr1:
                    item = arr1.pop()
                    if item.right:
                        arr2.append(item.right)
                        ans.append(item.right.val)
                    if item.left:
                        arr2.append(item.left)
                        ans.append(item.left.val)
            else:
                while arr2:
                    item = arr2.pop()
                    if item.left:
                        arr1.append(item.left)
                        ans.append(item.left.val)
                    if item.right:
                        arr1.append(item.right)
                        ans.append(item.right.val)
            if ans:
                res.append(ans)
            direction = not direction
        return res



a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a1.right = a3


a = Solution()
b = a.zigzagLevelOrder(
    a1
)
print(b)
