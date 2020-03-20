#!/usr/bin/python3
# Filename: test.py
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        info: List[accountInfo] = []
        for x in accounts:
            isIn = False
            for y in info:
                isIn = y.merge(x)
                a = 1
            if not isIn:
                info.append(accountInfo(len(info), x))
        return [[x.name] + x.emails for x in info]

class accountInfo:
    def __init__(self, idno: int, account: List[str]):
        self.id = idno
        self.name = account[0]
        self.emails = account[1:]
        self.__removeDuplicate__()
        self.emails.sort()

    def merge(self, account: List[str]) -> bool:
        if self.name == account[0] and any(self.__contains2__(x) for x in account):
            self.__merge__(account)
            return True
        else:
            return False

    def __contains2__(self, email: str) -> bool:
        low, high = 0, len(self.emails) - 1
        while low + 1 < high:
            mid = (low + high) // 2
            if self.emails[mid] == email:
                return True
            elif self.emails[mid] > email:
                high = mid
            elif self.emails[mid] < email:
                low = mid
        if self.emails[low] == email or self.emails[high] == email:
            return True
        return False

    def __merge__(self, account: List[str]):
        self.emails += account[1:]
        self.__removeDuplicate__()
        self.emails.sort()

    def __removeDuplicate__(self):
        arr = []
        for x in self.emails:
            if x not in arr:
                arr.append(x)
        self.emails = arr

a = Solution()
b = a.accountsMerge(
    [["Ethan","Ethan1@m.co","Ethan2@m.co","Ethan0@m.co"],
     ["David","David1@m.co","David2@m.co","David0@m.co"],
     ["Lily","Lily0@m.co","Lily0@m.co","Lily4@m.co"],
     ["Gabe","Gabe1@m.co","Gabe4@m.co","Gabe0@m.co"],
     ["Ethan","Ethan2@m.co","Ethan1@m.co","Ethan0@m.co"]]
)
print(b)
