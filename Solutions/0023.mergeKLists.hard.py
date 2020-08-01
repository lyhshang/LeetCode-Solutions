from typing import List
import heapq


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
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        heap = []
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
        root = ListNode(-1)
        tail = root
        while len(heap) > 0:
            v, index = heapq.heappop(heap)
            tail.next = lists[index]
            tail = tail.next
            lists[index] = lists[index].next
            if lists[index] is not None:
                heapq.heappush(heap, (lists[index].val, index))
        return root.next


if __name__ == '__main__':
    print(
        Solution().mergeKLists([
            ListNode.fromlist([1, 4, 5]),
            ListNode.fromlist([1, 3, 4]),
            ListNode.fromlist([2, 6]),
        ]).tolist(), [1, 1, 2, 3, 4, 4, 5, 6],
    )
