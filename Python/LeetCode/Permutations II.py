#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute(dic: collections.defaultdict, layer: int) -> List[List[int]]:
            if layer == 0:
                return [[]]
            res = []
            for key in dic:
                if dic[key] > 0:
                    dic[key] -= 1
                    ans = permute(dic, layer - 1)
                    for item in ans:
                        res.append([key] + item)
                    dic[key] += 1
            return res

        dic = collections.defaultdict(int)
        for n in nums:
            dic[n] += 1
        return permute(dic, len(nums))




a = Solution()
b = a.permuteUnique(
[1,1,2]
)
print(b)
