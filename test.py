#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:


a = Solution()
b = a.accountsMerge(
    [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
     ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
     ["David", "David1@m.co", "David2@m.co"]]
)
print(b)
