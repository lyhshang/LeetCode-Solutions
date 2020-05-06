from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = [[0 for j in i] for i in grid]

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or vis[i][j] == 1 or grid[i][j]=='0':
                return
            vis[i][j] = 1
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0' or vis[i][j] == 1:
                    continue
                res += 1
                dfs(i, j)
        return res


if __name__ == '__main__':
    print(
        Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]), 3,
        Solution().numIslands([]), 3,
    )
