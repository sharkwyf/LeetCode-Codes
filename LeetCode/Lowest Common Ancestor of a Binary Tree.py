#!/usr/bin/python3
# Filename: test.py
import null as null


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.dict = {}
        self.pindex = None
        self.qindex = None
        self.p = None
        self.q = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.helper(root, 1)
        pindex = self.pindex
        qindex = self.qindex
        while pindex != qindex:
            if pindex > qindex:
                pindex = pindex // 2
            else:
                qindex = qindex // 2
        return self.dict[pindex]

    def helper(self, node: 'TreeNode', index: int):
        if node == self.p:
            self.pindex = index
        if node == self.q:
            self.qindex = index
        self.dict[index] = node
        if node.left:
            self.helper(node.left, index * 2)
        if node.right:
            self.helper(node.right, index * 2 + 1)



a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a1.right = a3

a = Solution()
b = a.lowestCommonAncestor(
    a1, a1, a3
)
print(b)
