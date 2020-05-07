# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/6 23:32
"""
214. 最短回文串

给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1:

输入: "aacecaaa"
输出: "aaacecaaa"

示例 2:

输入: "abcd"
输出: "dcbabcd"
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        next = [-1 for i in range(len(s))]
        i = 0
        k = -1
        while i < len(s) - 1:
            if k == -1 or s[i] == s[k]:
                i += 1
                k += 1
                next[i] = k
            else:
                k = next[k]
        k = 0
        for i in range(len(s)-1, -1, -1):
            while k != -1 and s[i] != s[k]:
                k = next[k]
            k = k + 1
            if i <= k:
                return s[:-(len(s)-i-k+1):-1] + s
        return ""


if __name__ == '__main__':
    print(
        Solution().shortestPalindrome("aacecaaa"), "aaacecaaa",
        Solution().shortestPalindrome("abcd"), "dcbabcd",
    )