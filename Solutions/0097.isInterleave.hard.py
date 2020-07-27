# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/27 20:24
"""
97. 交错字符串

给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。



示例 1：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true

示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0:
                    dp[i][j] |= dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                if j > 0:
                    dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"), True)
    print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc"), False)
    print(Solution().isInterleave("", "", ""), True)
