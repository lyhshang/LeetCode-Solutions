# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/11 19:05
"""
treeArray
树状数组, a[1]-a[n]
O(log)单点更新、前缀和查询（区间查询）
"""


class TreeArray:
    lowbit = lambda x: x & -x

    def __init__(self, n):
        self.tree_array = [0 for i in range(n + 1)]
        self.n = n

    def update(self, index: int, v):
        while index <= self.n:
            self.tree_array[index] += v
            index += TreeArray.lowbit(index)

    def count(self, index: int):
        res = 0
        while index > 0:
            res += self.tree_array[index]
            index -= TreeArray.lowbit(index)
        return res
