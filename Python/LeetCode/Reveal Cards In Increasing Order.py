#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        lenD = len(deck)
        deck.sort(reverse=True)
        arr = []
        for i in range(lenD):
            arr = [deck[i]] + arr
            if 0 < i < lenD - 1:
                arr = [arr[-1]] + arr[0:-1]
        return arr


a = Solution()
b = a.deckRevealedIncreasing(
    [17,13,11,2,3,5,7]
)
print(b)
