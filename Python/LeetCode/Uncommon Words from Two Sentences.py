#!/usr/bin/python3
# Filename: test.py
from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        count = Counter(A.split(" ") + B.split(" "))
        return [x for x in count if count[x] == 1]


a = Solution()
b = a.uncommonFromSentences(
    A = "this apple is sweet", B = "this apple is sour"
)
print(list(b))
