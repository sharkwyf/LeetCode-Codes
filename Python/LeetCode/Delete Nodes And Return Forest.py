#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def DFS(root: TreeNode, to_delete: List[int], parent: TreeNode, sides: bool) -> List[TreeNode]:
            if not root:
                return []
            elif root.val in to_delete:
                res = DFS(root.left, to_delete, None, True) + DFS(root.right, to_delete, None, None)
                if parent:
                    if sides:
                        parent.left = None
                    else:
                        parent.right = None
                return res
            else:
                return ([root] if not parent else []) + DFS(root.left, to_delete, root, True) + DFS(root.right, to_delete, root, False)

        return DFS(root, to_delete, None, None)

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2; a1.right = a3

a = Solution()
b = a.delNodes(
    a1, [1]
)
print(b)
