# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/7 19:10
"""
kmp
字符串匹配
前缀next数组
O(n+m)匹配模式串
"""


def kmp(s: str, pattern: str) -> int:
    if len(pattern) == 0:
        return 0
    next = [-1 for i in range(len(pattern))]
    i = 0
    k = -1
    while i < len(pattern) - 1:
        if k == -1 or pattern[i] == pattern[k]:
            i += 1
            k += 1
            next[i] = k
        else:
            k = next[k]
    k = 0
    for i in range(len(s)):
        while k != -1 and s[i] != pattern[k]:
            k = next[k]
        k = k + 1
        if k == len(pattern):
            return i - k + 1
    return -1
