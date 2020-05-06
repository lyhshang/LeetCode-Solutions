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
    def swapPairs(self, head: ListNode) -> ListNode:
        root = ListNode(0)
        root.next = head
        temp = root
        while temp.next is not None:
            x = temp.next
            y = x.next
            if y is not None:
                x.next = y.next
                y.next = x
                temp.next = y
                temp = x
            else:
                break
        return root.next


if __name__ == '__main__':
    print(
        Solution().swapPairs(ListNode.fromlist(
            [1, 2, 3, 4])).tolist(), [2,1,4,3],
    )
