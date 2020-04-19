#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute1(dic: collections.defaultdict) -> List[List[int]]:
            ans = []
            for x in dic:
                if dic[x] > 0:
                    dic[x] -= 1
                    for y in permute1(dic):
                        ans.append([x] + y)
                    dic[x] += 1
            return ans if ans else [[]]

        dic = collections.defaultdict(int)
        for x in nums:
            dic[x] += 1
        return permute1(dic)





a = Solution()
b = a.permute(
    [1,2,3]
)
print(b)
