#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp_to_key(mycmp):
            'Convert a cmp= function into a key= function'

            class K:
                def __init__(self, obj, *args):
                    self.obj = obj

                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0

                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0

                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0

                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0

                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0

                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0

            return K

        def compare(x: int, y: int) -> int:
            d1, d2 = math.floor(math.log(x, 10)) + 1 if x > 0 else 1, math.floor(math.log(y, 10)) + 1 if y > 0 else 1
            xy = x * 10 ** d2 + y
            yx = y * 10 ** d1 + x
            return xy - yx

        return "".join([str(s) for s in sorted(nums, key=cmp_to_key(compare), reverse=True)]).lstrip('0') or '0'


a = Solution()
b = a.largestNumber(
    [1, 0, 0]
)
print(b)
