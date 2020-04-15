#!/usr/bin/python3
# Filename: test.py
from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        namedict = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                namedict[email] = name
        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                item = []
                while stack:
                    el = stack.pop()
                    item.append(el)
                    for x in graph[el]:
                        if x not in seen:
                            seen.add(x)
                            stack.append(x)
                ans.append([namedict[email]] + sorted(item))
        return ans


a = Solution()
b = a.accountsMerge(
    [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
     ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
)
print(b)
