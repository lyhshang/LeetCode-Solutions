# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/26 19:25
"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        dx = 1
        dy = 0
        y = 0
        x = 0
        h = len(matrix)
        if h == 0:
            return res
        w = len(matrix[0])
        for _ in range(h * w):
            res.append(matrix[y][x])
            matrix[y][x] = None
            if matrix[(y + dy) % h][(x + dx) % w] is None:
                dx, dy = -dy, dx
            x += dx
            y += dy
        return res


if __name__ == '__main__':
    print(
        Solution().spiralOrder(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
        ), [1, 2, 3, 6, 9, 8, 7, 4, 5],
    )
