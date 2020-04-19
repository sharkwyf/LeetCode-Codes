#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = 0
        dic = {}
        for x in answers:
            if x == 0:
                cnt += 1
            elif x not in dic:
                cnt += x + 1
                dic[x] = 1
            else:
                if dic[x] == x:
                    dic.pop(x)
                else:
                    dic[x] += 1
        return cnt



a = Solution()
b = a.numRabbits(
    [1,0,1,0,0]
)
print(b)
