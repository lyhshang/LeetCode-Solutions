"""
25. K 个一组翻转链表

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。



示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5



说明：

    你的算法只能使用常数的额外空间。
    你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        root = ListNode(0)
        pre = root
        pre.next = head
        while True:
            count = k - 1
            tail = pre.next
            if tail is None:
                break
            while count > 0 and tail.next is not None:
                temp = tail.next
                tail.next = temp.next
                temp.next = pre.next
                pre.next = temp
                count -= 1
            if count == 0:
                pre = tail
            else:
                for i in range(count, k - 1):
                    temp = pre.next
                    pre.next = temp.next
                    temp.next = tail.next
                    tail.next = temp
                break
        return root.next


if __name__ == '__main__':
    print(Solution().reverseKGroup(ListNode.fromlist([1, 2, 3, 4, 5]), 2).tolist(), [2, 1, 4, 3, 5])
    print(Solution().reverseKGroup(ListNode.fromlist([1, 2, 3, 4, 5]), 3).tolist(), [3, 2, 1, 4, 5])
    print(Solution().reverseKGroup(ListNode.fromlist([1, 2, 3]), 4).tolist(), [1, 2, 3])
