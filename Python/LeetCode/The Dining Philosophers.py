#!/usr/bin/python3
# Filename: test.py
import collections
from threading import Lock
from typing import List


class DiningPhilosophers:
    forks = [Lock() for _ in range(5)]
    fifth = [Lock()]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        if philosopher == 4:
            self.fifth[0].acquire()
            self.forks[philosopher % 5].acquire()
            self.forks[(philosopher + 1) % 5].acquire()
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
            self.forks[philosopher % 5].release()
            self.forks[(philosopher + 1) % 5].release()
            self.fifth[0].release()
        else:
            if philosopher == 3 or philosopher == 0:
                self.fifth[0].acquire()
            if philosopher % 2 == 0:
                self.forks[philosopher % 5].acquire()
                self.forks[(philosopher + 1) % 5].acquire()
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
                self.forks[philosopher % 5].release()
                self.forks[(philosopher + 1) % 5].release()
            else:
                self.forks[(philosopher + 1) % 5].acquire()
                self.forks[philosopher % 5].acquire()
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
                self.forks[philosopher % 5].release()
                self.forks[(philosopher + 1) % 5].release()
            if philosopher == 3 or philosopher == 0:
                self.fifth[0].release()



a = Solution()
b = a.numSquares(
    3102
)
print(b)
