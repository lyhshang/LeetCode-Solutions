# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/7/8 18:38
"""
206. 反转链表

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def tolist(self) -> list:
        res = [self.val]
        next_node = self.next
        while next_node is not None:
            res.append(next_node.val)
            next_node = next_node.next
        return res

    @classmethod
    def fromlist(cls, ls: list):
        head = ListNode(None)
        pre = head
        for i in ls:
            pre.next = ListNode(i)
            pre = pre.next
        return head.next


class Solution:
    def reverseList2(self, head: ListNode) -> ListNode:
        root = ListNode(-1)
        while head is not None:
            temp = head.next
            head.next = root.next
            root.next = head
            head = temp
        return root.next

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        next = head.next
        if next is not None:
            root = self.reverseList(next)
            next.next = head
            head.next = None
            return root
        return head


if __name__ == '__main__':
    print(
        Solution().reverseList(ListNode.fromlist([])).tolist(),
        Solution().reverseList(ListNode.fromlist([1,2,3,4,5])).tolist(),
    )