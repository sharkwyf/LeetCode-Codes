#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def intToRoman(self, num: int) -> str:
        i = 0
        res = ""
        while num:
            r = num % 10
            num = num // 10
            if 0 <= i < 3:
                if i == 0:
                    one, five, ten = "I", "V", "X"
                elif i == 1:
                    one, five, ten = "X", "L", "C"
                else:
                    one, five, ten = "C", "D", "M"
                if r == 4:
                    res = one + five + res
                elif r == 9:
                    res = one + ten + res
                else:
                    res = five * (r // 5) + one * (r % 5) + res
            else:
                one = "M"
                res = one * r + res
            i += 1
        return res


a = Solution()
b = a.intToRoman(
    1
)
print(b)