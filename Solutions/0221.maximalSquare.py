# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/8 21:50
"""
221. 最大正方形

在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""
from typing import List


class Solution:
    def getmax(self, tall: List[int]) -> int:
        res = 0
        q = [(-1, -1)]
        for i in range(len(tall)):
            lastindex = i
            while q[-1][0] > tall[i]:
                side = min(q[-1][0], i - q[-1][1])
                res = max(res, side * side)
                lastindex = q[-1][1]
                q.pop(-1)
            q.append((tall[i], lastindex))
        while q[-1][0] > 0:
            side = min(q[-1][0], len(tall) - q[-1][1])
            res = max(res, side * side)
            q.pop(-1)
        return res

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h = len(matrix)
        if h == 0:
            return 0
        w = len(matrix[0])
        tall = [0 for i in range(w)]
        res = 0
        for i in range(h):
            t = matrix[i]
            for j in range(w):
                tall[j] = tall[j] + 1 if t[j] == "1" else 0
            res = max(res, self.getmax(tall))
        return res


if __name__ == '__main__':
    print(Solution().maximalSquare([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]))