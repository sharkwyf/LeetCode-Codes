#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", r"%20")




a = Solution()
b = a.replaceSpace(
"We are happy."
)
print(b)
