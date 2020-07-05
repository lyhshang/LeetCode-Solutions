# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/5 10:39
"""
5454. 统计全 1 子矩形

给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。



示例 1：

输入：mat = [[1,0,1],
            [1,1,0],
            [1,1,0]]
输出：13
解释：
有 6 个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。

示例 2：

输入：mat = [[0,1,1,0],
            [0,1,1,1],
            [1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。

示例 3：

输入：mat = [[1,1,1,1,1,1]]
输出：21

示例 4：

输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5



提示：

    1 <= rows <= 150
    1 <= columns <= 150
    0 <= mat[i][j] <= 1
"""
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        h = len(mat)
        if h==0:
            return 0
        w = len(mat[0])
        if w==0:
            return 0
        dp = [[[[], 0] for j in range(w)] for i in range(h)]
        res = 0
        for i in range(h):
            for j in range(w):
                if mat[i][j] == 1:
                    dp[i][j][1] = dp[i-1][j][1]+1 if i!=0 else 1
                    pre = dp[i][j - 1][0] if j!=0 else []
                    le = len(pre)
                    now = dp[i][j][0]
                    for k in range(dp[i][j][1]):
                        if k < le:
                            now.append(pre[k] + 1)
                            res += pre[k] + 1
                        else:
                            now.append(1)
                            res += 1
        return res


if __name__ == '__main__':
    print(
        Solution().numSubmat(mat = [[1,0,1],
            [1,1,0],
            [1,1,0]])
    )
