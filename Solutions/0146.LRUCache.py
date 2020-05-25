# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/25 11:18
"""
146. LRU缓存机制

运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。



进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？



示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

Your LRUCache object will be instantiated and called as such:
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)
"""
import collections


class NODE:
    def __init__(self, key, v):
        self.key = key
        self.v = v
        self.pre = None
        self.next = None

    def append(self, n):
        self.next.pre = n
        n.next = self.next
        n.pre = self
        self.next = n

    def remove(self):
        self.pre.next = self.next
        self.next.pre = self.pre
        self.next = None
        self.pre = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = [[] for i in range(capacity)]
        self.root = NODE(None, None)
        self.tail = NODE(None, None)
        self.root.next = self.tail
        self.tail.pre = self.root
        self.length = 0

    def hash(self, key):
        hkey = key % self.capacity
        for i in range(len(self.hashmap[hkey])):
            if key == self.hashmap[hkey][i].key:
                return hkey, i
        return hkey, -1

    def get(self, key: int) -> int:
        hi, hj = self.hash(key)
        if hj == -1:
            return -1
        else:
            node = self.hashmap[hi][hj]
            self.move_to_top(node)
            return node.v

    def put(self, key: int, value: int) -> None:
        hi, hj = self.hash(key)
        if hj == -1:
            node = NODE(key, value)
            self.root.append(node)
            self.hashmap[hi].append(node)
            self.length += 1
        else:
            node = self.hashmap[hi][hj]
            node.v = value
            self.move_to_top(node)

        if self.length > self.capacity:
            node = self.tail.pre
            node.remove()
            hi, hj = self.hash(node.key)
            self.hashmap[hi].pop(hj)
            self.length -= 1

    def move_to_top(self, n: NODE):
        n.remove()
        self.root.append(n)


class LRUCache2(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


if __name__ == '__main__':
    obj = LRUCache(4)
    for i in range(6):
        obj.put(i, i*10)
    for i in range(6):
        print(obj.get(i))
        pass
