# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/19 16:07
"""
680. 验证回文字符串 Ⅱ

给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True

示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。

注意:

    字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalidrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        l = 0
        r = len(s) - 1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                if isPalidrome(s[l+1:r+1]):
                    return True
                if isPalidrome(s[l:r]):
                    return True
                return False
        return True


if __name__ == '__main__':
    print(
        Solution().validPalindrome("aba"),
        Solution().validPalindrome("abccbaa"),
    )