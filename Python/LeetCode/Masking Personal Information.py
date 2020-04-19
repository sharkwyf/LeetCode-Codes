#!/usr/bin/python3
# Filename: test.py
from typing import List
import re

class Solution:
    def maskPII(self, S: str) -> str:
        name = r"[a-zA-Z]{2,}"
        email = r"^{0}@{0}.{0}$".format(name)
        phone = r"^[0-9+\-() ]{10,}$"
        if re.match(email, S):
            return (S[0] + "*****" + S[S.index(r"@") - 1:]).lower()
        elif re.match(phone, S):
            str = re.sub(r"[+\-() ]", "", S)
            return ("+{0}-".format("*" * (len(str) - 10)) if len(str) > 10 else "") + "***-***-{0}".format(str[-4:])
        else:
            pass
        return email

a = Solution()
b = a.maskPII(
    "86-(10)12345678"
)
print(b)
