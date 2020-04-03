#!/usr/bin/python3
# Filename: test.py
import collections
from typing import List


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        len_num = len(num)
        for i in range(1, len_num // 2 + 1):
            for j in range(i + 1, (len_num + i) // 2 + 1):
                prev, next = int(num[:i]), int(num[i:j])
                if prev != 0 and num[:i].startswith("0"):
                    continue
                if next != 0 and num[i:j].startswith("0"):
                    continue
                remain = num[j:]
                while remain:
                    sum = prev + next
                    if len(str(sum)) > len(remain) or int(remain[:len(str(sum))]) != sum:
                        break
                    elif len(str(sum)) == len(remain):
                        return True
                    else:
                        prev, next = next, sum
                        remain = remain[len(str(sum)):]
        return False


a = Solution()
b = a.isAdditiveNumber(
    "0235813"
)
print(b)
