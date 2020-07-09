# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/8 19:49
"""
199. 二叉树的右视图

给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        def update(node, k):
            if node is not None:
                if k < len(res):
                    res[k] = node.val
                else:
                    res.append(node.val)
                update(node.left, k+1)
                update(node.right, k+1)
        update(root, 0)
        return res
