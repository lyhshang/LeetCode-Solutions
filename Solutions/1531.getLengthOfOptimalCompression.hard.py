# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/26 10:06
"""
1531. 压缩字符串 II

行程长度编码 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。例如，用此方法压缩字符串 "aabccc" ，将 "aa" 替换为 "a2" ，"ccc" 替换为` "c3" 。因此压缩后的字符串变为 "a2bc3" 。

注意，本问题中，压缩时没有在单个字符后附加计数 '1' 。

给你一个字符串 s 和一个整数 k 。你需要从字符串 s 中删除最多 k 个字符，以使 s 的行程长度编码长度最小。

请你返回删除最多 k 个字符后，s 行程长度编码的最小长度 。



示例 1：

输入：s = "aaabcccd", k = 2
输出：4
解释：在不删除任何内容的情况下，压缩后的字符串是 "a3bc3d" ，长度为 6 。最优的方案是删除 'b' 和 'd'，这样一来，压缩后的字符串为 "a3c3" ，长度是 4 。

示例 2：

输入：s = "aabbaa", k = 2
输出：2
解释：如果删去两个 'b' 字符，那么压缩后的字符串是长度为 2 的 "a4" 。

示例 3：

输入：s = "aaaaaaaaaaa", k = 0
输出：3
解释：由于 k 等于 0 ，不能删去任何字符。压缩后的字符串是 "a11" ，长度为 3 。



提示：

    1 <= s.length <= 100
    0 <= k <= s.length
    s 仅包含小写英文字母
"""


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if k >= len(s):
            return 0

        def count_val(count: int) -> int:
            if count >= 100:
                return 4
            elif count >= 10:
                return 3
            elif count >= 2:
                return 2
            else:
                return 1
        z = len(s)
        dp = [[-1 for j in range(len(s) - k + 1)] for i in range(len(s))]
        for i in range(z - 1, -1, -1):
            # dp[i][0] = 0
            for j in range(1, z - k + 1):
                if i + j > z:
                    # dp[i][j] = -1
                    break
                count = 0
                remain = j
                min_value = 1000
                for t in range(i, len(s)):
                    if s[t] == s[i]:
                        count += 1
                        remain -= 1
                    else:
                        if dp[t][remain] == -1:
                            break
                        min_value = min(min_value, count_val(count) + dp[t][remain])
                    if remain == 0:
                        min_value = min(min_value, count_val(count))
                        break
                dp[i][j] = min_value
        res = 1000
        for i in range(k + 1):
            res = min(res, dp[i][len(s) - k])
        return res


if __name__ == '__main__':
    print(Solution().getLengthOfOptimalCompression("aaabcccd", 2), 4)
    print(Solution().getLengthOfOptimalCompression("aabbaa", 2), 2)
    print(Solution().getLengthOfOptimalCompression("aaaaaaaaaaa", 0), 3)
    print(Solution().getLengthOfOptimalCompression("bbabbbabbbbcbb", 4), 3)
    print(Solution().getLengthOfOptimalCompression("aabaabbcbbbaccc", 6), 4)
