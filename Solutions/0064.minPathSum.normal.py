# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/8/3 10:17
"""
64. 最小路径和

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        w = len(grid[0])
        dp = [[float('inf') for j in range(w)] for i in range(2)]
        index = 1
        dp[index][0] = 0
        for i in range(len(grid)):
            index ^= 1
            dp[index][0] = dp[index ^ 1][0] + grid[i][0]
            for j in range(1, w):
                dp[index][j] = min(
                    dp[index ^ 1][j], dp[index][j - 1]) + grid[i][j]
        return dp[index][-1]


if __name__ == '__main__':
    print(Solution().minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]), 7)
