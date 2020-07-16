# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/16 19:01
"""
297. 二叉树的序列化与反序列化

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例:

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"

提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def tolist(self) -> list:
        res = []

        def ser(node):
            if node is None:
                res.append(None)
            else:
                res.append(node.val)
                ser(node.left)
                ser(node.right)
        ser(self)
        while len(res) > 0 and res[-1] is None:
            res.pop()
        return res

    @classmethod
    def fromlist(cls, data: list):
        index = 0

        def des():
            nonlocal index
            if index >= len(data) or data[index] is None:
                index += 1
                return None
            else:
                node = TreeNode(data[index])
                index += 1
                node.left = des()
                node.right = des()
                return node
        return des()


class Codec:
    def serialize(self, root):
        res = []

        def ser(node):
            if node is None:
                res.append(None)
            else:
                res.append(node.val)
                ser(node.left)
                ser(node.right)
        ser(root)
        return res

    def deserialize(self, data):
        index = 0

        def des():
            nonlocal index
            if data[index] is None:
                index += 1
                return None
            else:
                node = TreeNode(data[index])
                index += 1
                node.left = des()
                node.right = des()
                return node
        return des()


if __name__ == '__main__':
    codec = Codec()
    root = TreeNode.fromlist([1, 2, None, None, 3, 4])
    print(
        codec.deserialize(codec.serialize(root)).tolist()
    )
