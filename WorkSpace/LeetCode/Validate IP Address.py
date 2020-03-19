#!/usr/bin/python3
# Filename: test.py
import re


class Solution(object):
    def validIPAddress(self, IP: str) -> str:
        """
        :type IP: str
        :rtype: str
        """

        "Test the segment if it's IPv4's format"

        def __is_IPv4(s: str) -> bool:
            try:
                x = int(s)
                if (0 <= x & x < 256) & (re.match(r"^([1-9][0-9]{0,2}|0)$", s) != None):
                    return True
                return False
            except ValueError:
                return False

        "Test the segment if it's IPv6's format"

        def __is_IPv6(s: str) -> bool:
            if re.match("^[0-9a-fA-F]{1,4}$", s) != None:
                return True
            return False

        arr = re.split(r"\.", IP)
        if len(arr) == 4:
            isIPv4 = True
            for x in arr:
                if not __is_IPv4(x):
                    isIPv4 = False
                    break
            if isIPv4:
                return "IPv4"
        arr = list()
        arr = re.split(r":", IP)
        if len(arr) == 8:
            isIPv6 = True
            for x in arr:
                if not __is_IPv6(x):
                    isIPv6 = False
                    break
            if isIPv6:
                return "IPv6"
        return "Neither"

a = Solution()
print(a.validIPAddress("172.16.254.1"))