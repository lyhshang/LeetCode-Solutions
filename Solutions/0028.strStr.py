# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/6 23:11
"""
28. 实现 strStr()

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        pre = [-1 for i in range(len(needle))]
        for i in range(1, len(needle)):
            temp = pre[i - 1]
            while temp != -1 and needle[i] != needle[temp + 1]:
                temp = pre[temp]
            pre[i] = temp + 1 if needle[i] == needle[temp + 1] else -1
        index = -1
        for i in range(len(haystack)):
            while index != -1 and haystack[i] != needle[index + 1]:
                index = pre[index]
            if haystack[i] == needle[index + 1]:
                index += 1
                if index == len(needle) - 1:
                    return i - index
        return -1


if __name__ == '__main__':
    print(
        Solution().strStr("hello", "ll"), 2,
        Solution().strStr("aaaaa", "bba"), -1,
    )
