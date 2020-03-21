#!/usr/bin/python3
# Filename: test.py
from typing import List
import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foolock = threading.Lock()
        self.barlock = threading.Lock()
        self.barlock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.foolock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.barlock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.barlock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foolock.release()

a = FooBar(10)
_thread.start_new_thread(a.foo, )
_thread.start_new_thread()



# a = Solution()
# b = a.accountsMerge(
#     [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
#      ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]
# )
# print(b)
