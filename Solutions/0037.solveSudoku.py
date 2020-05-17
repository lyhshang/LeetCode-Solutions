# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/17 9:59
"""
37. 解数独

编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

空白格用 '.' 表示。

一个数独。

答案被标成红色。

Note:

    给定的数独序列只包含数字 1-9 和字符 '.' 。
    你可以假设给定的数独只有唯一解。
    给定数独永远是 9x9 形式的。
"""
from typing import List


class Board:
    def __init__(self, board):
        self.board = board
        self.vis = [[{i: 0 for i in range(1, 10)}
                     for x in range(9)] for y in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    self.update(i, j, int(board[i][j]))

    def update(self, i, j, v):
        for k in range(9):
            self.vis[i][k][v] += 1
            self.vis[k][j][v] += 1
        x = i // 3
        y = j // 3
        for xx in range(3):
            for yy in range(3):
                self.vis[x * 3 + xx][y * 3 + yy][v] += 1
        self.board[i][j] = str(v)

    def undo(self, i, j, v):
        for k in range(9):
            self.vis[i][k][v] -= 1
            self.vis[k][j][v] -= 1
        x = i // 3
        y = j // 3
        for xx in range(3):
            for yy in range(3):
                self.vis[x * 3 + xx][y * 3 + yy][v] -= 1
        self.board[i][j] = '.'

    def getnext(self, x):
        for xx in range(x, 81):
            i = xx // 9
            j = xx % 9
            if self.board[i][j] == '.':
                return xx
        return -1

    def solve(self, x):
        if x == -1:
            return True
        i = x // 9
        j = x % 9
        res = False
        for k, v in self.vis[i][j].items():
            if v==0:
                self.update(i, j, k)
                if self.solve(self.getnext(x + 1)):
                    res = True
                    break
                self.undo(i, j, k)
        return res


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        B = Board(board)
        B.solve(B.getnext(0))


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board)
    for z in board:
        print(z)
