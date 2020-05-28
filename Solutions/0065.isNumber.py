# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/28 16:02
"""
65. 有效数字

验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

    数字 0-9
    指数 - "e"
    正/负号 - "+"/"-"
    小数点 - "."

当然，在输入中，这些字符的上下文也很重要。
"""


class Node:
    def __init__(self):
        self.next = {}

    def setnext(self, s, n):
        self.next[s] = n

    def get(self, s):
        return self.next.get(s, -1)


class DFA:
    def __init__(self, nums):
        self.nodes = [Node() for i in range(nums)]

    def go(self, s):
        index = 0
        for c in s:
            index = self.nodes[index].get(c)
            if index == -1:
                break
        return index

    def set(self, ss, ns):
        for i in range(len(ns)):
            for j in range(len(ns[i])):
                for s in ss[j]:
                    self.nodes[i].setnext(s, ns[i][j])


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        state blank +/- 0-9 . e
        0 	0 	1 	6 	2 	-1
        1 	-1 	-1 	6 	2 	-1
        2 	-1 	-1 	3 	-1 	-1
        3 	8 	-1 	3 	-1 	4
        4 	-1 	7 	5 	-1 	-1
        5 	8 	-1 	5 	-1 	-1
        6 	8 	-1 	6 	3 	4
        7 	-1 	-1 	5 	-1 	-1
        8 	8 	-1 	-1 	-1 	-1
        """
        dfa = DFA(9)
        ss = [[' '], ['+', '-'], [str(i) for i in range(10)], ['.'], ['e']]
        ns = [[0, 1, 6, 2, -1],
              [-1, -1, 6, 2, -1],
              [-1, -1, 3, -1, -1],
              [8, -1, 3, -1, 4],
              [-1, 7, 5, -1, -1],
              [8, -1, 5, -1, -1],
              [8, -1, 6, 3, 4],
              [-1, -1, 5, -1, -1],
              [8, -1, -1, -1, -1], ]
        dfa.set(ss, ns)
        res = dfa.go(s)
        return res in [3, 5, 6, 8]


if __name__ == '__main__':
    print(
        Solution().isNumber(" 0.1 "),
        Solution().isNumber("95a54e53"),
        Solution().isNumber("."),
        Solution().isNumber(" "),
    )
