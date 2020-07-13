# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/13 16:48
"""
295. 数据流的中位数

中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

    void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    double findMedian() - 返回目前所有元素的中位数。

示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

进阶:

    如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
    如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
"""
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap_low = []
        self.heap_high = []

    def addNum(self, num: int) -> None:
        if len(self.heap_low) == 0 or num <= -self.heap_low[0]:
            heapq.heappush(self.heap_low, -num)
        else:
            heapq.heappush(self.heap_high, num)
        while len(self.heap_low) < len(self.heap_high):
            v = heapq.heappop(self.heap_high)
            heapq.heappush(self.heap_low, -v)
        while len(self.heap_low) > len(self.heap_high) + 1:
            v = -heapq.heappop(self.heap_low)
            heapq.heappush(self.heap_high, v)

    def findMedian(self) -> float:
        if len(self.heap_low) == len(self.heap_high):
            a = -self.heap_low[0] if len(self.heap_low) > 0 else 0
            b = self.heap_high[0] if len(self.heap_high) > 0 else 0
            return (a + b) / 2
        else:
            return -self.heap_low[0] if len(self.heap_low) > 0 else 0


if __name__ == '__main__':
    median = MedianFinder()
    median.addNum(-1)
    print(median.findMedian())
    median.addNum(-2)
    print(median.findMedian())
    median.addNum(-3)
    print(median.findMedian())
    median.addNum(-4)
    print(median.findMedian())
    median.addNum(-5)
    print(median.findMedian())
