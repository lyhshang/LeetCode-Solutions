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
        nodes = []
        while head is not None:
            nodes.append(head)
            head = head.next
        if n == len(nodes):
            if len(nodes) <= 1:
                return None
            else:
                return nodes[1]
        else:
            nodes[-n - 1].next = nodes[-n].next
            return nodes[0]


if __name__ == '__main__':
    print(
        Solution().removeNthFromEnd(ListNode.fromlist(
            [1, 2, 3, 3, 5]), 2).tolist(), [1, 2, 3, 5],
    )
