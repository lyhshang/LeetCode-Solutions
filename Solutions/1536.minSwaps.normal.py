# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/8/2 10:24
"""
1536. 排布二进制网格的最少交换次数

给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。

一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。

请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。

主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。



示例 1：

输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
输出：3

示例 2：

输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
输出：-1
解释：所有行都是一样的，交换相邻行无法使网格符合要求。

示例 3：

输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
输出：0



提示：

    n == grid.length
    n == grid[i].length
    1 <= n <= 200
    grid[i][j] 要么是 0 要么是 1 。
"""
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        temp = {i: [] for i in range(n)}
        for i in range(n):
            count = n - 1
            for j in range(n - 1, 0, -1):
                if grid[i][j] == 0:
                    count -= 1
                else:
                    break
            temp[count].append(i)
        offset = [0 for i in range(n)]
        res = 0
        import heapq
        hp = []
        for i in range(n):
            for k in temp[i]:
                heapq.heappush(hp, k)
            if len(hp) == 0:
                return -1
            k = heapq.heappop(hp)
            real_k = k + offset[k]
            res += real_k - i
            for j in range(k):
                offset[j] += 1
        return res


if __name__ == '__main__':
    print(Solution().minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]), 3)
    print(Solution().minSwaps([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]), -1)
    print(Solution().minSwaps([[1, 0, 0], [1, 1, 0], [1, 1, 1]]), 0)
    print(Solution().minSwaps([[1, 0, 0, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 1, 0, 0]]), 2)
