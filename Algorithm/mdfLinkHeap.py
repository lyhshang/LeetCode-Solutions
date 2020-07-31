# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/14 13:41
"""
LinkHeap
链表堆
链表和堆的结合，结点维护链表的前驱、后继以及在堆中的坐标
"""


class Node:
    def __init__(self, v):
        self.v = v

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
        return self.v < other.v

    def __str__(self):
        return "({}, {})".format(self.v, self.index)


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
        """
        修改节点值后，重新调整堆结构
        :param index:被修改的节点坐标
        :return:
        """
        self._down(index)
        self._up(index)

    def push(self, n: Node):
        """
        添加节点
        :param n:节点
        :return:
        """
        n.index = len(self.heap)
        self.heap.append(n)
        self.update(n.index)

    def pop(self, index=0) -> [Node, None]:
        """
        删除节点
        :param index: 删除的节点坐标
        :return: 删除的节点
        """
        if index >= len(self.heap):
            return None
        res = self.heap[index]
        self.heap[index] = self.heap[-1]
        self.heap[index].index = index
        self.heap.pop()
        self.update(index)
        return res

    def top(self) -> [Node, None]:
        """
        堆顶节点
        :return: 堆顶节点
        """
        return self.heap[0] if len(self.heap) > 0 else None

    def __len__(self):
        return len(self.heap)


if __name__ == '__main__':
    ns = [Node(10 - i) for i in range(10)]
    heap = LinkHeap()
    for i in range(len(ns)):
        if i >0:
            Node.link(ns[i], ns[i-1])
        heap.push(ns[i])
    while True:
        top = heap.pop()
        if top is None:
            break
        else:
            print(str(top), str(top.next) if top.next is not None else None, str(top.pre) if top.pre is not None else None)
            Node.drop(top)
