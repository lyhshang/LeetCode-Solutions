# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/6 22:55
"""
21. 合并两个有序链表

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        temp = root
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        while l1 is not None:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
        while l2 is not None:
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        return root.next
