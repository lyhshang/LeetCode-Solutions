# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/30 11:16
"""
58. 最后一个单词的长度

给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。



示例:

输入: "Hello World"
输出: 5
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = -1
        last = -1
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                last = i
                break
        for i in range(last):
            if s[i] == ' ':
                index = i
        return last-index


if __name__ == '__main__':
    print(
        Solution().lengthOfLastWord("Hello World"),
        Solution().lengthOfLastWord(" Hello  "),
        Solution().lengthOfLastWord(""),
    )