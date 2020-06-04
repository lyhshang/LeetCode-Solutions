# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/6/4 19:31
"""
76. 最小覆盖子串

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

说明：

    如果 S 中不存这样的子串，则返回空字符串 ""。
    如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        temp = {}
        count = 0
        resi = len(s)
        resj = 0

        for c in t:
            if target.get(c) is None:
                target[c] = 1
                temp[c] = 0
                count += 1
            else:
                target[c] += 1

        j = 0
        for i in range(len(s)):
            if s[i] in temp:
                temp[s[i]] += 1
                if temp[s[i]] == target[s[i]]:
                    count -= 1
            if count == 0:
                while j <= i:
                    if s[j] not in temp:
                        j += 1
                    elif temp[s[j]]>target[s[j]]:
                        temp[s[j]] -= 1
                        j += 1
                    else:
                        break
                if i-j < resi-resj:
                    resi, resj = i, j
        return s[resj:resi+1] if resi<len(s) else ""


if __name__ == '__main__':
    print(
        Solution().minWindow("ADOBECODEBANC", "ABC"),
    )