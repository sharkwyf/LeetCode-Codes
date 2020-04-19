#!/usr/bin/python3
# Filename: test.py
import collections
from threading import Lock
from typing import List


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        self.integer = value
        self.arr = []

    """
    If value is not specified, initializes an empty list.
    Otherwise initializes a single integer equal to value.
    """

    def isInteger(self):
        return self.integer is not None

    """
    @return True if this NestedInteger holds a single integer, rather than a nested list.
    :rtype bool
    """

    def add(self, elem):
        self.arr.append(elem)

    """
    Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
    :rtype void
    """

    def setInteger(self, value):
        self.integer = value

    """
    Set this NestedInteger to hold a single integer equal to value.
    :rtype void
    """

    def getInteger(self):
        return self.integer

    """
    @return the single integer that this NestedInteger holds, if it holds a single integer
    Return None if this NestedInteger holds a nested list
    :rtype int
    """

    def getList(self):
        return self.arr

    """
    @return the nested list that this NestedInteger holds, if it holds a nested list
    Return None if this NestedInteger holds a single integer
    :rtype List[NestedInteger]
    """


import re


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def DFS(s: str) -> NestedInteger:
            if not s:
                return None
            if re.match(r"^\[.*\]$", s):
                s = s[1:-1]
                cnt = 0
                arr = []
                i = 0
                for j in range(len(s)):
                    if s[j] == "[":
                        cnt += 1
                    elif s[j] == "]":
                        cnt -= 1
                    elif s[j] == "," and cnt == 0:
                        if j > i:
                            arr.append(s[i:j])
                            i = j + 1
                if s[i:]:
                    arr.append(s[i:])
                nest = NestedInteger()
                for x in arr:
                    nest.add(DFS(x))
                return nest
            else:
                if re.match(r"^[\-]{0,1}[\d]+$", s):
                    return NestedInteger(int(s))

        return DFS(s)


a = Solution()
b = a.deserialize(
    "[1,2,3]"
)
print(b)
