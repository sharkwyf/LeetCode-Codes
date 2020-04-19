#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def check(word: str, dic: collections.defaultdict) -> bool:
            if all(dic[k] == 0 for k in dic):
                return True
            else:
                while word:
                    if word[0] in dic and dic[word[0]] > 0:
                        dic[word[0]] -= 1
                        if check(word[1:], dic):
                            dic[word[0]] += 1
                            return True
                        else:
                            dic[word[0]] += 1
                            return False
                    word = word[1:]
                return False

        dic = collections.defaultdict(int)
        for x in licensePlate:
            if x.isalpha():
                dic[x.lower()] += 1
        words.sort(key=len)
        for w in words:
            if check(w, dic):
                return w


a = Solution()
b = a.shortestCompletingWord(
    licensePlate = "stew", words = ["looks", "pest", "stew", "show"]
)
print(b)
