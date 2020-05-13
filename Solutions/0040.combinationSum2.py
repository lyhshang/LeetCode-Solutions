# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/13 10:17
from typing import List


class Solution:
    def combinationSum2(
            self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.l = len(candidates)
        self.candidates = candidates
        self.res = []
        self.path = []
        self.dfs(target, 0)
        return self.res

    def dfs(self, target: int, start: int):
        if target == 0:
            self.res.append(self.path.copy())
        for i in range(start, self.l):
            if i > start and self.candidates[i] == self.candidates[i-1]:
                continue
            num = self.candidates[i]
            if target - num < 0:
                break
            self.path.append(num)
            self.dfs(target - num, i + 1)
            self.path.pop(-1)
