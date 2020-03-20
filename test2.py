#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans


a = Solution()
b = a.accountsMerge(
    [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
     ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
     ["David", "David1@m.co", "David2@m.co"]]
)
print(b)


