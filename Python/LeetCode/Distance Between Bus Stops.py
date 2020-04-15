#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from typing import List
import re


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        d1 = sum(distance[:min(start, destination)]) + sum(distance[max(start, destination):])
        d2 = sum(distance[min(start, destination): max(start, destination)])
        return min(d1, d2)




a = Solution()
b = a.distanceBetweenBusStops(
    distance = [1,2,3,4], start = 0, destination = 1
)
print(b)