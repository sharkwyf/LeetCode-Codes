#!/usr/bin/python3
# Filename: test.py
import collections
from threading import Lock
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if not data:
            return True
        low = 0
        for i in range(0, len(data)):
            if i == low:
                # Check if it's the starter & Set the New 'high'
                if 0 <= data[i] < 128:
                    low = i + 1
                elif 192 <= data[i] < 224:
                    low = i + 2
                elif 224 <= data[i] < 240:
                    low = i + 3
                elif 240 <= data[i] < 248:
                    low = i + 4
                else:
                    return False
            else:
                # Check if it starts with "01"
                if 128 <= data[i] < 192:
                    continue
                else:
                    return False
        return low == len(data)


a = Solution()
b = a.validUtf8(
    [235, 140, 4]
)
print(b)
