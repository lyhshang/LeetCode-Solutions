# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/12 9:55
"""
1513. 仅含 1 的子串数

给你一个二进制字符串 s（仅由 '0' 和 '1' 组成的字符串）。

返回所有字符都为 1 的子字符串的数目。

由于答案可能很大，请你将它对 10^9 + 7 取模后返回。



示例 1：

输入：s = "0110111"
输出：9
解释：共有 9 个子字符串仅由 '1' 组成
"1" -> 5 次
"11" -> 3 次
"111" -> 1 次

示例 2：

输入：s = "101"
输出：2
解释：子字符串 "1" 在 s 中共出现 2 次

示例 3：

输入：s = "111111"
输出：21
解释：每个子字符串都仅由 '1' 组成

示例 4：

输入：s = "000"
输出：0



提示：

    s[i] == '0' 或 s[i] == '1'
    1 <= s.length <= 10^5
"""


class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        pre = 0
        mod = int(1e9 + 7)
        for c in s:
            if c == '1':
                pre += 1
                res += pre
                res %= mod
            else:
                pre = 0
        return res


if __name__ == '__main__':
    print(
        Solution().numSub(nums=[5, 3, 2, 4]),
    )
