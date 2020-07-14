# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/13 23:55
"""
188. 买卖股票的最佳时机 IV

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
"""
from typing import List


class Node:
    def __init__(self, dv, mv):
        self.dv = dv    # 删除损失
        self.mv = mv    # 归并损失

        self.pre = None
        self.next = None
        self.index = 0

    @classmethod
    def link(cls, left, right):
        if isinstance(left, cls):
            left.next = right
        if isinstance(right, cls):
            right.pre = left

    @classmethod
    def drop(cls, n):
        if isinstance(n, cls):
            if isinstance(n.pre, cls):
                n.pre.next = n.next
            if isinstance(n.next, cls):
                n.next.pre = n.pre
            n.pre, n.next = None, None

    def __lt__(self, other):
        return min(self.dv, self.mv) < min(other.dv, other.mv)


class LinkHeap:
    def __init__(self):
        self.heap = []
        self.root = None
        self.end = None

    def _up(self, index):
        while index > 0:
            f = (index - 1) // 2
            if self.heap[index] < self.heap[f]:
                self.heap[f], self.heap[index] = self.heap[index], self.heap[f]
                self.heap[f].index = f
                self.heap[index].index = index
                index = f
            else:
                break

    def _down(self, index):
        left = index * 2 + 1
        while left < len(self.heap):
            target = index
            right = left + 1
            if self.heap[left] < self.heap[target]:
                target = left
            if right < len(self.heap) and self.heap[right] < self.heap[target]:
                target = right
            if target == index:
                break
            self.heap[target], self.heap[index] = self.heap[index], self.heap[target]
            self.heap[target].index = target
            self.heap[index].index = index
            index = target
            left = index * 2 + 1

    def update(self, index):
        self._down(index)
        self._up(index)

    def push(self, n: Node):
        n.index = len(self.heap)
        self.heap.append(n)
        self.update(n.index)

    def pop(self, index=0) -> [Node, None]:
        if index >= len(self.heap):
            return None
        res = self.heap[index]
        self.heap[index] = self.heap[-1]
        self.heap[index].index = index
        self.heap.pop()
        self.update(index)
        return res

    def top(self) -> [Node, None]:
        return self.heap[0] if len(self.heap) > 0 else None

    def __len__(self):
        return len(self.heap)


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        k = min(k, len(prices) // 2)
        if k == 0 or len(prices) == 0:
            return 0

        # 根据价格升序创建交易区间
        sales = []
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                if buy < prices[i-1]:
                    sales.append((buy, prices[i-1]))
                buy = prices[i]
        sales.append((buy, prices[-1]))

        # 统计各区间删除、归并的损失，向左归并，头区间不能删除
        profits = LinkHeap()
        left = Node(sales[0][1] - sales[0][0], int(1e9))
        profits.push(left)
        for i in range(1, len(sales)):
            right = Node(sales[i][1] - sales[i][0], sales[i - 1][1] - sales[i][0])
            Node.link(left, right)
            profits.push(right)
            left = right

        # 贪心归并区间
        while len(profits) > k:
            # 查损失最小区间
            n = profits.top()

            # 删除、归并区间
            if n.dv < n.mv:
                if n.next is not None:
                    n.next.mv += n.mv - n.dv
                    profits.update(n.next.index)
                profits.pop(n.index)
                Node.drop(n)
            else:
                n.pre.dv += n.dv - n.mv
                profits.update(n.pre.index)
                profits.pop(n.index)
                Node.drop(n)

        # 统计收益
        res = 0
        for n in profits.heap:
            res += n.dv
        return res


if __name__ == '__main__':
    print(Solution().maxProfit(2, [2, 4, 1]), 2)
    print(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]), 7)
    print(Solution().maxProfit(3, [2]), 0)
    print(Solution().maxProfit(0, [2, 4, 1]), 0)
