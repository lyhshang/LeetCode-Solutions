# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/6 22:47
"""
20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

示例 2:

输入: "()[]{}"
输出: true

示例 3:

输入: "(]"
输出: false

示例 4:

输入: "([)]"
输出: false

示例 5:

输入: "{[]}"
输出: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        m = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c == '(' or c == '[' or c == '{':
                q.append(m[c])
            else:
                if len(q) > 0 and q[-1] == c:
                    q.pop(-1)
                else:
                    return False
        if len(q) == 0:
            return True
        return False


if __name__ == '__main__':
    print(Solution().isValid("{[]}"),True)
