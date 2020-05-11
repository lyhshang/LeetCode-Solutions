# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/7 19:07
"""
manachar
最长回文子串
O(n)找最长回文子串
"""


def manachar(s: str) -> str:
    temp = "#"
    for c in s:
        temp += c + "#"
    maxl = [0 for i in range(len(temp))]
    maxr = -1
    mid = -1
    res = 0
    for i in range(len(temp)):
        maxl[i] = maxl[2 * mid - i] if i <= maxr else 0
        while i + maxl[i] + 1 < len(temp) and i - maxl[i] - 1 >= 0 and temp[i + maxl[i] + 1] == temp[i - maxl[i] - 1]:
            maxl[i] += 1
        if maxl[i] > maxr:
            maxr = maxl[i]
            mid = i
        res = max(res, mid[i])
    return res
