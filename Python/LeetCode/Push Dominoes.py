#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        len_d = len(dominoes)
        dis = []
        d = -1
        for i in range(len_d):
            if dominoes[i] == "L":
                d = -1
                dis.append(-1)
            elif dominoes[i] == "R":
                d = i
                dis.append(0)
            elif d == -1:
                dis.append(-1)
            else:
                dis.append(i - d)
        d = -1
        for i in range(len_d - 1, - 1, - 1):
            if dominoes[i] == "L":
                d = i
                dis[i] = "L"
            elif d == - 1:
                dis[i] = "." if dis[i] == - 1 else "R"
            elif dis[i] == - 1:
                dis[i] = "L"
            elif dis[i] == 0:
                d = - 1
                dis[i] = "R"
            else:
                if d - i > dis[i]:
                    dis[i] = "R"
                elif d - i == dis[i]:
                    dis[i] = "."
                else:
                    dis[i] = "L"
        return "".join(dis)



a = Solution()
b = a.pushDominoes(
    ".L.R...LR..L.."
)
print(b)
