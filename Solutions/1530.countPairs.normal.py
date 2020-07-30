# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/26 10:06
"""
1530. 好叶子节点对的数量

给你二叉树的根节点 root 和一个整数 distance 。

如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。

返回树中 好叶子节点对的数量 。



示例 1：



输入：root = [1,2,3,null,4], distance = 3
输出：1
解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。

示例 2：

输入：root = [1,2,3,4,5,6,7], distance = 3
输出：2
解释：好叶子节点对为 [4,5] 和 [6,7] ，最短路径长度都是 2 。但是叶子节点对 [4,6] 不满足要求，因为它们之间的最短路径长度为 4 。

示例 3：

输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
输出：1
解释：唯一的好叶子节点对是 [2,5] 。

示例 4：

输入：root = [100], distance = 1
输出：0

示例 5：

输入：root = [1,1,1], distance = 2
输出：1



提示：

    tree 的节点数在 [1, 2^10] 范围内。
    每个节点的值都在 [1, 100] 之间。
    1 <= distance <= 10
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0

        def dfs(node: TreeNode) -> dict:
            dis_dict = {i: 0 for i in range(distance)}
            if node is None:
                return dis_dict
            if node.left is None and node.right is None:
                dis_dict[0] = 1
                return dis_dict
            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            for i in range(distance):
                for j in range(distance - i - 1):
                    res += left[i] * right[j]
                if i + 1 < distance:
                    dis_dict[i + 1] = left[i] + right[i]
            return dis_dict
        dfs(root)
        return res


if __name__ == '__main__':
    print(Solution().countPairs(TreeNode.fromlist([1, 2, 3, None, 4]), 3), 1)
    print(Solution().countPairs(TreeNode.fromlist([1, 2, 3, 4, 5, 6, 7]), 3), 2)
    print(Solution().countPairs(TreeNode.fromlist([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]), 3), 1)
    print(Solution().countPairs(TreeNode.fromlist([100]), 1), 0)
    print(Solution().countPairs(TreeNode.fromlist([1, 1, 1]), 2), 1)
