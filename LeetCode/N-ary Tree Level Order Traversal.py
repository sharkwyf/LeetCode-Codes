#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List



# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        dq = collections.deque()
        dq.append(root)
        res = []
        while dq:
            item = []
            for i in range(len(dq)):
                r = dq.popleft()
                if r.children:
                    dq.extend(r.children)
                item.append(r.val)
            res.append(item)
        return res


a = Solution()
b = a.findFrequentTreeSum(
    a1
)
print(b)
