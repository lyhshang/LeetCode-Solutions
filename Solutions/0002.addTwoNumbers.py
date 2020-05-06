"""
# 2. 两数相加

## 题意

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例1:**
```
输入: (2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 0 -> 8
原因: 342 + 465 = 807
```

## 题解
简单的链表处理问题。

因为数字数逆序存储的，所以头节点就是最低位，符合数字计算的自然顺序。
将两个链表头节点对齐，按顺序计算两节点值与进位之和，注意模10并进位。
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        head.next = ListNode(0)
        res = head
        c = 0
        while l1 is not None or l2 is not None or c > 0:
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0
            res.next = ListNode((a + b + c) % 10)
            c = (a + b + c) // 10
            res = res.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return head.next


if __name__ == '__main__':
    l1 = ListNode.fromlist([2, 4, 3])
    l2 = ListNode.fromlist([5, 6, 4])
    print(
        Solution().addTwoNumbers(l1, l2).tolist()
    )
