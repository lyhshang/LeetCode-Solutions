from typing import List


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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 2:
            head = ListNode(0)
            temp, x, y = head, lists[0], lists[1]
            while x is not None and y is not None:
                if x.val <= y.val:
                    temp.next = x
                    x = x.next
                else:
                    temp.next = y
                    y = y.next
                temp = temp.next
            if x is not None:
                temp.next = x
            else:
                temp.next = y
            return head.next
        elif len(lists) > 2:
            res = []
            for i in range(len(lists) // 2):
                res.append(self.mergeKLists([lists[i * 2], lists[i * 2 + 1]]))
            if len(lists) % 2 == 1:
                res.append(lists[-1])
            return self.mergeKLists(res)
        elif len(lists) == 1:
            return lists[0]
        else:
            return None


if __name__ == '__main__':
    print(
        Solution().mergeKLists([
            ListNode.fromlist([1, 4, 5]),
            ListNode.fromlist([1, 3, 4]),
            ListNode.fromlist([2, 6]),
        ]).tolist(), [1, 1, 2, 3, 4, 4, 5, 6],
    )
