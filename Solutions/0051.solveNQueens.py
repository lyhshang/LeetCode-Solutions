# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/21 20:20
"""
51. N皇后

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

提示：

    皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自 百度百科 - 皇后 ）
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        temp = [['.']*n for i in range(n)]
        vis = [[True]*n for i in range(2)] + [[True]*2*n for i in range(2)]
        def dfs(i):
            if i>=n:
                res.append([''.join(i) for i in temp])
                return
            for j in range(n):
                if vis[0][i] and vis[1][j] and vis[2][i+j] and vis[3][i-j]:
                    vis[0][i] = vis[1][j] = vis[2][i + j] = vis[3][i - j] = False
                    temp[i][j] = 'Q'
                    dfs(i+1)
                    vis[0][i] = vis[1][j] = vis[2][i + j] = vis[3][i - j] = True
                    temp[i][j] = '.'
        dfs(0)
        return res


if __name__ == '__main__':
    print(
        Solution().solveNQueens(4),
    )