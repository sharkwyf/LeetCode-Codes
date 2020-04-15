#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def isNumber(self, s: str) -> bool:
        num_pat = r"[0-9]+(\.[0-9]+){0,1}"
        a1 = re.match(r"^[\+\-]{0,1}" + num_pat + "$", s)
        a2 = re.match(r"^[\-]{0,1}" + num_pat + "[eE]]" + r"[\-]{0,1}" + num_pat + "$", s)
        if re.match(r"^[\+\-]{0,1}" + num_pat + "$", s) \
                or re.match(r"^[\-]{0,1}" + num_pat + "[eE]]" + r"[\-]{0,1}" + num_pat + "$", s):
            return True
        else:
            return False



a = Solution()
b = a.isNumber(
    "5e2"
)
print(b)
