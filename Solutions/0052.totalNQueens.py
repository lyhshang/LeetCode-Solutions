# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/21 20:55
"""
52. N皇后 II

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]



提示：

    皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或七步，可进可退。（引用自 百度百科 - 皇后 ）
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        vis = [[True] * n for i in range(2)] + [[True] * 2 * n for i in range(2)]

        def dfs(i):
            if i >= n:
                self.res += 1
                return
            for j in range(n):
                if vis[0][i] and vis[1][j] and vis[2][i + j] and vis[3][i - j]:
                    vis[0][i] = vis[1][j] = vis[2][i + j] = vis[3][i - j] = False
                    dfs(i + 1)
                    vis[0][i] = vis[1][j] = vis[2][i + j] = vis[3][i - j] = True

        dfs(0)
        return self.res


if __name__ == '__main__':
    print(
        Solution().totalNQueens(4),
    )
