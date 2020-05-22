# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/22 11:11
"""
105. 从前序与中序遍历序列构造二叉树

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mybuildTree(self, pl: int, il: int, length: int) -> TreeNode:
        if length <= 0:
            return None
        n = TreeNode(self.preorder[pl])
        index = self.index[n.val]
        n.left = self.mybuildTree(pl+1, il, index-il)
        n.right = self.mybuildTree(pl+1+index-il, index+1, il+length-index-1)
        return n

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder
        self.inorder = inorder
        self.index = {}
        for i in range(len(inorder)):
            self.index[inorder[i]] = i
        return self.mybuildTree(0, 0, len(preorder))

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 用栈迭代
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorderindex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderindex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while len(stack) > 0 and stack[-1].val == inorder[inorderindex]:
                    node = stack.pop(-1)
                    inorderindex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)
        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = Solution().buildTree(preorder, inorder)
    def prtree(n, level):
        if n is not None:
            print(n.val, level)
            prtree(n.left, level+1)
            prtree(n.right, level+1)
    prtree(root,0)
