#!/usr/bin/python3
# Filename: test.py
import collections
import math
import random
from functools import reduce
from typing import List
import re


class CQueue:

    def __init__(self):
        self.instack = True
        self.stack = []
        self.aux = []

    def appendTail(self, value: int) -> None:
        if self.instack:
            self.stack.append(value)
        else:
            self.instack = True
            while self.aux:
                self.stack.append(self.aux.pop())
            self.stack.append(value)

    def deleteHead(self) -> int:
        if self.instack:
            if not self.stack:
                return -1
            self.instack = False
            while len(self.stack) > 1:
                self.aux.append(self.stack.pop())
            return self.stack.pop()
        else:
            if not self.aux:
                return -1
            return self.aux.pop()





a = Solution()
b = a.replaceSpace(
"We are happy."
)
print(b)
