# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/23 11:31
"""
63. 不同路径 II

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(w)] for i in range(2)]
        index = 0

        dp[index][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for j in range(1, w):
            dp[index][j] = dp[index][j - 1] if obstacleGrid[0][j] == 0 else 0
        for i in range(1, h):
            index ^= 1
            dp[index][0] = dp[index ^ 1][0] if obstacleGrid[i][0] == 0 else 0
            for j in range(1, w):
                dp[index][j] = dp[index ^ 1][j] + dp[index][j - 1] if obstacleGrid[i][j] == 0 else 0
        return dp[index][-1]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles(
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    ), 2)
    print(Solution().uniquePathsWithObstacles(
        [
            [1],
        ]
    ), 0)
