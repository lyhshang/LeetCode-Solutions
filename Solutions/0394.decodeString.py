# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/28 22:28
"""
394. 字符串解码

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
"""


class Solution:
    def decodeString(self, s: str) -> str:
        index = 0
        count = 0
        res = ""
        num = 0
        for i in range(len(s)):
            if s[i] == '[':
                if count == 0:
                    index = i+1
                count += 1
            elif s[i] == ']':
                count -= 1
                if count == 0:
                    res += self.decodeString(s[index:i]) * num
                    num = 0
            elif 0 <= ord(s[i]) - ord('0') < 10:
                if count == 0:
                    num *= 10
                    num += ord(s[i]) - ord('0')
            else:
                if count == 0:
                    res += s[i]
        return res


if __name__ == '__main__':
    print(
        Solution().decodeString("3[a]2[bc]"),
        Solution().decodeString("3[a2[c]]"),
    )
