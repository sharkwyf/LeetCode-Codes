#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        arr = []
        for x in accounts:
            for item in arr:
                isIn = True
                if item[0] != x[0]:
                    continue
                if item[1:].index()


a = Solution()
print(a.accountsMerge(
    [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
))
