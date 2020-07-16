# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/16 19:04
"""
329. 矩阵中的最长递增路径

给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。

示例 2:

输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
"""
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        h = len(matrix)
        w = len(matrix[0])
        dp = [[0 for j in range(w)] for i in range(h)]
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def get(y, x):
            if dp[y][x] == 0:
                dp[y][x] = 1
                for dx, dy in d:
                    if 0 <= y + dy < h \
                            and 0 <= x + dx < w \
                            and matrix[y + dy][x + dx] > matrix[y][x]:
                        dp[y][x] = max(dp[y][x], get(y + dy, x + dx) + 1)
            return dp[y][x]

        res = 0
        for i in range(h):
            for j in range(w):
                res = max(res, get(i, j))
        return res


if __name__ == '__main__':
    print(
        Solution().longestIncreasingPath(
            [
                [3, 4, 5],
                [3, 2, 6],
                [2, 2, 1]
            ]
        )
    )
    print(
        Solution().longestIncreasingPath(
            [[1, 2]]
        )
    )
