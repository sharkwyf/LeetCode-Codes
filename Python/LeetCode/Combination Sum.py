#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combineSum(candidates: List[int], target: int) -> List[List[int]]:
            if target in dic:
                return dic[target]
            else:
                for i, x in enumerate(candidates):
                    if x == target:
                        ans = [0] * len(candidates)
                        ans[i] = 1
                        dic[target].append(ans)
                    elif x < target:
                        ans = combineSum(candidates, target - x)
                        for item in ans:
                            it = item.copy()
                            it[i] += 1
                            dic[target].append(it)
                return dic[target]

        dic = collections.defaultdict(list)
        ans = combineSum(candidates, target)
        items = []
        for x in ans:
            if x not in items:
                items.append(x)
        res = []
        for item in items:
            x = []
            for i in range(len(candidates)):
                x += [candidates[i]] * item[i]
            res.append(x)
        return res



a = Solution()
b = a.combinationSum(
    candidates = [2,3,6,7], target = 7
)
print(b)
