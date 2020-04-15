#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:

    def __init__(self, nums: List[int]):
        self.dic = collections.defaultdict(list)
        for i, v in enumerate(nums):
            if v not in self.dic:
                self.dic[v].append(1)
                self.dic[v].append([i, i])
            elif self.dic[v][-1][1] + 1 == i:
                self.dic[v][0] += 1
                self.dic[v][-1][1] = i
            else:
                self.dic[v][0] += 1
                self.dic[v].append([i, i])

    def pick(self, target: int) -> int:
        item = self.dic[target]
        idx = random.randint(1, item[0])
        i = 1
        while idx > 0:
            if idx > item[i][1] - item[i][0] + 1:
                idx -= item[i][1] - item[i][0] + 1
                i += 1
            else:
                return item[i][0] + idx - 1


a = Solution([1,2,3,3,3])
for i in range(30):
    b = a.pick(3)
# b = a.numFriendRequests(
#     [73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]
# )
    print(b)
