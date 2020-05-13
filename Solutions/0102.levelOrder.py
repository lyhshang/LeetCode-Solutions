# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/13 10:45
"""
102. 二叉树的层序遍历

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。



示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = [(root, 0)]
        while len(q) > 0:
            node, level = q[0]
            q.pop(0)
            if node is None:
                continue
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
        return res


if __name__ == '__main__':
    num = [None, 3, 9, 20, None, None, 15, 7]
    nodes = [TreeNode(i) if i is not None else None for i in num]
    for i in range(2, len(nodes)):
        if nodes[i] is None:
            continue
        if i%2 == 0:
            nodes[i//2].left = nodes[i]
        else:
            nodes[i // 2].right = nodes[i]
    print(Solution().levelOrder(nodes[1]))
