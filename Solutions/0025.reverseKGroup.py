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
        root.next = head
        tail = root
        pre = root
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail:
                break
            nr = pre.next
            while pre.next != tail:
                cur = pre.next
                pre.next = cur.next
                cur.next = tail.next
                tail.next = cur
            pre, tail = nr, nr
        return root.next


if __name__ == '__main__':
    print(
        Solution().reverseKGroup(ListNode.fromlist(
            [1, 2, 3, 4, 5]), 2).tolist(), [2, 1, 4, 3, 5],
        Solution().reverseKGroup(ListNode.fromlist(
            [1, 2, 3, 4, 5]), 3).tolist(), [3, 2, 1, 4, 5],
    )
