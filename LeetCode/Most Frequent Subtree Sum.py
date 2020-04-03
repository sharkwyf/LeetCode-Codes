#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def DFS(r: TreeNode):
            if r:
                ans.append(r.val + DFS(r.left) + DFS(r.right))
                return ans[-1]
            else:
                return 0

        ans = []
        if not root:
            return []
        DFS(root)
        Counter = collections.Counter(ans)
        lenC = Counter.most_common(1)[0][1]
        return [x for x, y in Counter.items() if y == lenC]



a1 = TreeNode(5)
a2 = TreeNode(2)
a3 = TreeNode(-3)
a1.left = a2
a1.right = a3

a = Solution()
b = a.findFrequentTreeSum(
    a1
)
print(b)
