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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tail = head
        for i in range(n - 1):
            tail = tail.next
        root = ListNode(0)
        root.next = head
        while tail.next is not None:
            root = root.next
            tail = tail.next
        if root.next is head:
            root.next = root.next.next
            return root.next
        else:
            root.next = root.next.next
            return head


if __name__ == '__main__':
    print(Solution().removeNthFromEnd(ListNode.fromlist([1, 2, 3, 4, 5]), 2).tolist(), [1, 2, 3, 5])
    print(Solution().removeNthFromEnd(ListNode.fromlist([1, 2]), 1).tolist(), [2])
