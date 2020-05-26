# -*- coding: utf-8 -*-
# author:lyh
# datetime:2020/5/26 19:17
"""
floydCycleDetection
弗洛伊德判圈法
O(n)时间找到链表中环的起点
"""
from typing import List


def floydCycleDetection(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


if __name__ == '__main__':
    print(
        # 1->3->2->4->2
        floydCycleDetection([1, 3, 4, 2, 2]),
        # 3->4->2->3
        floydCycleDetection([3, 1, 3, 4, 2]),
    )
