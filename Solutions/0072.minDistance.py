# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/6/3 16:12
"""
72. 编辑距离

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

    插入一个字符
    删除一个字符
    替换一个字符



示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[100000 for j in range(len(word2) + 1)]
              for i in range(2)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    dp[i % 2][j] = max(i, j)
                elif word1[i - 1] == word2[j - 1]:
                    dp[i % 2][j] = 1 + min(dp[i % 2][j - 1],
                                           dp[(i - 1) % 2][j],
                                           dp[(i - 1) % 2][j - 1] - 1)
                else:
                    dp[i % 2][j] = 1 + min(dp[i % 2][j - 1],
                                           dp[(i - 1) % 2][j],
                                           dp[(i - 1) % 2][j - 1])
        return dp[len(word1) % 2][len(word2)]


if __name__ == '__main__':
    print(
        Solution().minDistance(word1="horse", word2="ros"),
        Solution().minDistance(word1="intention", word2="execution"),
    )
