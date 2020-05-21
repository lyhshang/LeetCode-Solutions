# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/21 20:07
"""
49. 字母异位词分组

给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：

    所有输入均为小写字母。
    不考虑答案输出的顺序。
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0 for i in range(26)]
            for c in s:
                count[ord(c)-ord('a')] += 1
            t = res.get(tuple(count), None)
            if t is None:
                t = res[tuple(count)] = []
            t.append(s)
        return list(res.values())


if __name__ == '__main__':
    print(
        Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
    )
