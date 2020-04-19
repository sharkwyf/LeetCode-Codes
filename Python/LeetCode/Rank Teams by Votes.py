#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Solution:
    def rankTeams(self, votes):
        cnt = {v: [0] * len(votes[0]) + [v] for v in votes[0]}
        for vote in votes:
            for i, v in enumerate(vote):
                cnt[v][i] -= 1
        return "".join(sorted(votes[0], key=cnt.get))


a = Solution()
b = a.rankTeams(
    ["ABC","ACB","ABC","ACB","ACB"]
)
print(b)
