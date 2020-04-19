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
    def sumNumbers(self, root: TreeNode) -> int:
        def DFS(root: TreeNode) -> List[List[int]]:
            if root:
                if not root.left and not root.right:
                    return [[root.val]]
                else:
                    ans = DFS(root.left) + DFS(root.right)
                    for x in ans:
                        x.append(root.val)
                    return ans
            else:
                return []

        return sum(sum(li[i] * 10 ** i for i in range(len(li))) for li in DFS(root))


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a1.right = a3

a = Solution()
b = a.sumNumbers(
    a1
)
print(b)
