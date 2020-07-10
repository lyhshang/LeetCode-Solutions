# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/11 0:16
"""
103. 二叉树的锯齿形层次遍历

给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def tolist(self) -> list:
        def getdict(node: TreeNode, index):
            if node is None:
                return {}
            else:
                res = {index: node.val}
                res.update(getdict(node.left, index * 2 + 1))
                res.update(getdict(node.right, index * 2 + 2))
            return res

        rd = getdict(self, 0)
        res = []
        for key, value in rd.items():
            while key >= len(res):
                res.append(None)
            res[key] = value
        return res

    @classmethod
    def fromlist(cls, ls: list):
        nodes = []
        for i in range(len(ls)):
            node = TreeNode(ls[i]) if ls[i] is not None else None
            nodes.append(node)
            if i % 2 == 0:
                nodes[(i - 1) // 2].right = node
            else:
                nodes[(i - 1) // 2].left = node
        return nodes[0]


class Solution:
    def zigzagLevelOrder2(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res

        q = [[], []]
        qindex = 0
        q[qindex].append(root)
        res.append([root.val])

        while len(q[qindex]) > 0:
            temp = []
            for i in range(len(q[qindex]) - 1, -1, -1):
                node = q[qindex][i]
                if qindex == 0:
                    if node.right is not None:
                        temp.append(node.right.val)
                        q[1].append(node.right)
                    if node.left is not None:
                        temp.append(node.left.val)
                        q[1].append(node.left)
                else:
                    if node.left is not None:
                        temp.append(node.left.val)
                        q[0].append(node.left)
                    if node.right is not None:
                        temp.append(node.right.val)
                        q[0].append(node.right)
            if len(temp) > 0:
                res.append(temp)
            q[qindex].clear()
            qindex = (qindex + 1) % 2
        return res

    def zigzagLevelOrder(self, root):
        """
        代码源自leecode@keewa
        """
        nodes = [(root,)]
        values = []
        step = 1
        while nodes:
            values.append([r.val for n in nodes[::step] for r in n[::step] if r])
            step = -step
            nodes = [(r.left, r.right) for n in nodes for r in n if r]
        return values[:-1]


if __name__ == '__main__':
    print(
        Solution().zigzagLevelOrder(
            TreeNode.fromlist([3, 9, 20, None, None, 15, 7])),
    )
