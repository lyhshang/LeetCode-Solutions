# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/30 11:26
"""
59. 螺旋矩阵 II

给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[-1 for i in range(n)] for j in range(n)]
        dx = 1
        dy = 0
        y = 0
        x = 0
        if n == 0:
            return res
        for i in range(1, n*n+1):
            res[y][x] = i
            if res[(y + dy) % n][(x + dx) % n] != -1:
                dx, dy = -dy, dx
            x += dx
            y += dy
        return res


if __name__ == '__main__':
    print(
        Solution().generateMatrix(3)
    )