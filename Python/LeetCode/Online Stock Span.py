#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.arr and self.arr[-1][0] <= price:
            cnt += self.arr.pop()[1]
        self.arr.append([price, cnt])
        return cnt

a = StockSpanner()
a.next(31)
a.next(41)
a.next(48)
a.next(59)
a.next(79)
a.next(11)


# a = Solution()
# b = a.minSwap(
#     A = [1,3,5,4,5,6,7,8], B = [1,2,3,7,8,9,10,11]
# )
# print(b)