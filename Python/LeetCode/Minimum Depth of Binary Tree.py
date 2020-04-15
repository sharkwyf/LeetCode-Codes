#!/usr/bin/python3
# Filename: test.py
import null as null

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def minheight(root: TreeNode) -> int:
            if root == None:
                return 0;
            else:
                left = minheight(root.left)
                right = minheight(root.right)
                if left == 0 and right == 0:
                    return 1
                if left == 0:
                    return right + 1
                if right == 0:
                    return left + 1
                return left + 1 if left < right else right + 1

        return minheight(root)

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a2.left = a3

a = Solution()
b = a.minDepth(
    a1
)
print(b)
