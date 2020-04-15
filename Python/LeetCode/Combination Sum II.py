#!/usr/bin/python3
# Filename: test.py
from typing import List
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from functools import lru_cache
        def DFS(candidates: List[int], target: int, result: List[int], results: List[List[int]]):
            if target == 0 and result not in results:
                results.append(result)
            lenC = len(candidates)
            if lenC == 0:
                return
            if candidates[0] <= target:
                DFS(candidates[1:], target - candidates[0], result + [candidates[0]], results)
            for i in range(1, lenC):
                if candidates[i] <= target:
                    DFS(candidates[i:], target, result, results)
                    break

        results = []
        candidates.sort(reverse=True)
        DFS(candidates, target, [], results)
        return results


a = Solution()
b = a.combinationSum2(
    [10, 1, 2, 7, 6, 1, 5], target=8,
)
print(b)
