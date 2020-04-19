#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class LinkNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.list = LinkNode(None)
        self.list.left = self.list
        self.list.right = self.list
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key][1]
            prev, next = node.left, node.right
            prev.right = next
            next.left = prev
            node.left = self.list
            node.right = self.list.right
            node.left.right = node
            node.right.left = node
            return self.dic[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key][0] = value
            node = self.dic[key][1]
            prev, next = node.left, node.right
            prev.right = next
            next.left = prev
            node.left = self.list
            node.right = self.list.right
            node.left.right = node
            node.right.left = node
        else:
            node = LinkNode(key, self.list, self.list.right)
            node.left.right = node
            node.right.left = node
            self.dic[key] = [value, node]
            if len(self.dic) > self.cap:
                self.dic.pop(self.list.left.val)
                self.list.left = self.list.left.left
                self.list.left.right = self.list


a = LRUCache(2)
a.put(2,1)
a.put(1,1)
a.put(2,3)
a.put(4,1)
a1 = a.get(1)
a2 = a.get(2)

#
# a = Solution()
# b = a.largestNumber(
#     [1, 0, 0]
# )
# print(b)
