#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List
import re

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters)
        while low < high:
            mid = (low + high) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return letters[high % len(letters)]

a = Solution()
b = a.nextGreatestLetter(
["b","e","e","e","e","e","n","n","n","s"],
"a"
)
print(b)
