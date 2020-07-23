# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/23 11:18
"""
62. 不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？



示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:

输入: m = 7, n = 3
输出: 28



提示：

    1 <= m, n <= 100
    题目数据保证答案小于等于 2 * 10 ^ 9
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for j in range(n)] for i in range(2)]
        index = 0
        for i in range(1, m):
            index ^= 1
            dp[index][0] = dp[index ^ 1][0]
            for j in range(1, n):
                dp[index][j] = dp[index ^ 1][j] + dp[index][j - 1]
        return dp[index][-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(1, 1), 1)
    print(Solution().uniquePaths(3, 2), 3)
    print(Solution().uniquePaths(7, 3), 28)
