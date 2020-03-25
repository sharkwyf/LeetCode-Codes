#!/usr/bin/python3
# Filename: test.py
from collections import deque
import null as null


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pindex = root.index(p)
        qindex = root.index(q)
        while pindex != qindex:
            if pindex > qindex:
                pindex = (pindex + 1) // 2 - 1
            else:
                qindex = (qindex + 1) // 2 - 1
        return root[pindex]


a = Solution()
b = a.lowestCommonAncestor(
    [-1, 0, 3, -2, 4, null, null, 8],
3,
8
)
print(b)
