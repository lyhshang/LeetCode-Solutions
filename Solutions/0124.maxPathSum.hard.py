# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/10 0:41
"""
124. 二叉树中的最大路径和

给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6

示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
"""


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
    def __maxSum(self, x: TreeNode) -> int:
        if x is None:
            return 0
        l = max(self.__maxSum(x.left), 0)
        r = max(self.__maxSum(x.right), 0)
        self.res = max(self.res, l + r + x.val)
        return max(l, r) + x.val

    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        self.__maxSum(root)
        return self.res


if __name__ == '__main__':
    print(
        Solution().maxPathSum(TreeNode.fromlist([1, 2, 3])), 6,
        Solution().maxPathSum(TreeNode.fromlist([-10, 9, 20, None, None, 15, 7])), 42,
        Solution().maxPathSum(TreeNode.fromlist([1, -2, 3])), 4,
    )
