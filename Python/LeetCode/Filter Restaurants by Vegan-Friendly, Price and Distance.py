#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = [r for r in restaurants if not ((veganFriendly and not r[2]) or r[3] > maxPrice or r[4] > maxDistance)]
        return [r[0] for r in sorted(res, key=lambda x: x[0:2][::-1], reverse=True)]


a = Solution()
b = a.filterRestaurants(
    [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
    0,
    50,
    10
)
print(b)
