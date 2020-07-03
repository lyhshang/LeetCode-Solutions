# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/3 21:05
"""
61. 旋转链表

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def fromlist(cls, vs):
        head = None
        for v in vs[::-1]:
            n = head
            head = ListNode(v)
            head.next = n
        return head

    @classmethod
    def tolist(cls, head):
        vs = []
        while head is not None:
            vs.append(head.val)
            head = head.next
        return vs


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        p = head
        l = 1
        while p.next is not None:
            p = p.next
            l += 1
        p.next = head
        for i in range(l - k % l):
            p = p.next
        head = p.next
        p.next = None
        return head


if __name__ == '__main__':
    head_1 = ListNode.fromlist([1, 2, 3, 4, 5])
    res_1 = ListNode.tolist(Solution().rotateRight(head_1, 2))
    head_2 = ListNode.fromlist([0, 1, 2])
    res_2 = ListNode.tolist(Solution().rotateRight(head_2, 4))
    print(
        res_1, [4, 5, 1, 2, 3],
        res_2, [2, 0, 1],
    )
