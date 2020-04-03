#!/usr/bin/python3
# Filename: test.py
import collections
import math
from typing import List
import re


class Codec:
    def __init__(self):
        self.idx = 0
        self.dict = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.dict[self.idx] = longUrl
        self.idx += 1
        return "http://tinyurl.com/" + str(self.idx - 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if len(shortUrl) > 19:
            id = int(shortUrl[19:])
            if id in self.dict:
                return self.dict[id]
        return ""


a = Solution()
b = a.delNodes(
    a1, [1]
)
print(b)
